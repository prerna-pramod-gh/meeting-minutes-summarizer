import openai
import os

# Set your API key (you can export it from your environment)
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_transcript(transcript):
    prompt = f"""
You are a meeting assistant. Summarize the following meeting transcript in 3-5 sentences. Then, list clear action points as bullet points.

Transcript:
\"\"\"
{transcript}
\"\"\"

Your output format:
Summary:
[summary]

Action Points:
- [point 1]
- [point 2]
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    full_response = response["choices"][0]["message"]["content"]

    # Simple parsing
    if "Action Points:" in full_response:
        summary_part, action_part = full_response.split("Action Points:", 1)
        summary = summary_part.replace("Summary:", "").strip()
        action_points = ["- " + line.strip("- ").strip() for line in action_part.strip().split("\n") if line.strip()]
    else:
        summary = full_response.strip()
        action_points = []

    return summary, action_points
