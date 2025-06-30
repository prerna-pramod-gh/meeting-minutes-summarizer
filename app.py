from flask import Flask, request, render_template_string, jsonify
from ai_utils import summarize_transcript

app = Flask(__name__)

with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

@app.route("/")
def index():
    return render_template_string(html_template)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    transcript = data.get("transcript", "")
    if not transcript.strip():
        return jsonify({"error": "Transcript is empty."}), 400
    summary, action_points = summarize_transcript(transcript)
    return jsonify({
        "summary": summary,
        "action_points": action_points
    })

if __name__ == "__main__":
    app.run(debug=True)
