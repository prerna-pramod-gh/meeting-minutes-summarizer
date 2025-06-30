# meeting-minutes-summarizer

# 1. Clone the repository
git clone https://github.com/your-username/meeting-minutes-summarizer.git
cd meeting-minutes-summarizer

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API key
export OPENAI_API_KEY=your-key-here  # On Windows: set OPENAI_API_KEY=your-key-here

# 5. Run the Flask app
python app.py
