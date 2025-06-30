
# 📝 Meeting Minutes Summarizer (AI-Powered)

This is a simple AI-powered web app that takes raw meeting transcripts and summarizes them into:
- A short summary (3–5 lines)
- A list of clear action points

Built with **Flask**, **OpenAI GPT**, and a minimal **HTML frontend** (no external static folders), it is lightweight and easy to run locally.

---

## 🚀 Features

- Paste your meeting transcript in the browser  
- AI generates concise summaries using OpenAI GPT  
- Lists actionable bullet points from the conversation  
- Inline HTML/CSS/JS – no `/static` folder  

---

## 🛠 Tech Stack

- Python + Flask  
- OpenAI GPT API  
- HTML + CSS (inline)  

---

## 🧪 Running Locally

```bash
# Clone the repo
git clone https://github.com/your-username/meeting-minutes-summarizer.git
cd meeting-minutes-summarizer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API Key
export OPENAI_API_KEY=your-key-here  # Windows: set OPENAI_API_KEY=your-key-here

# Run the app
python app.py
````

## 📚 License
MIT

---

👩‍💻 Made by Prerna Pramod 
---



