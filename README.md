# 📝 Meeting Minutes Summarizer (AI-Powered)

This project is a simple AI-powered web app that takes raw meeting transcripts and summarizes them into:
- A short summary (3–5 lines)
- A list of clear action points

Built using **Flask**, **OpenAI's GPT model**, and a minimal **HTML-only frontend** (no external static folders), it's designed to be lightweight, fast, and developer-friendly.

---

## 🚀 Features
- 🔹 Paste your meeting transcript directly in the browser  
- 🤖 AI generates concise summaries using OpenAI GPT (e.g., `gpt-3.5-turbo`)  
- ✅ Lists actionable bullet points from the conversation  
- 📦 No `/static` folder – all HTML/CSS/JS is inline  
- 🧠 Future-ready for publishing on platforms like ReadyTensor  

---

## 🛠 Tech Stack
- Python + Flask  
- OpenAI GPT API  
- HTML + CSS (inline)  
- Optional: jQuery (not required)  
- No database, no external folders – everything is flat-structured  

---

## 🧪 Run the Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/meeting-minutes-summarizer.git
cd meeting-minutes-summarizer

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API Key
export OPENAI_API_KEY=your-key-here  # Windows: set OPENAI_API_KEY=your-key-here

# 5. Run the Flask app
python app.py



👩‍💻 Made by Prerna Pramod
