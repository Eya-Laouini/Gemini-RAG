import os
import google.generativeai as genai
from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
import markdown
from PyPDF2 import PdfReader

# Configure the Flask app
app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)  # More secure random key

Session(app)

# Configure Google Gemini API
GEMINI_API_KEY = "PUT_YOUR_API_KEY"
if not GEMINI_API_KEY:
    raise ValueError("Google Gemini API key not set.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Read and process the PDF file
PDF_FILE_PATH = r"C:\Users\LENOVO\Desktop\Fine-Tuning-Gemini\Fake_Persons_Info.pdf"  
policy_content = ""

if os.path.exists(PDF_FILE_PATH):
    reader = PdfReader(PDF_FILE_PATH)
    policy_content = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
else:
    raise FileNotFoundError(f"PDF file not found at {PDF_FILE_PATH}")

# Define routes
@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        user_message = request.form['message']
        prompt = f"""
        You are an AI assistant answering questions strictly based on the provided document.
        Extract relevant information and provide concise answers.
        
        Document content:
        {policy_content}
        
        User query:
        {user_message}
        
        If the answer is not found in the document, state: "The information is not available in the provided document."
        """
        try:
            response = model.generate_content(prompt).text.strip()
        except Exception as e:
            response = f"Error generating response: {str(e)}"

        ai_response_html = markdown.markdown(response)
        session['chat_history'].append((user_message, ai_response_html))
        session.modified = True

        return redirect(url_for('chat'))

    return render_template('chat.html', chat_history=session['chat_history'])

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['chat_history'] = []
    session.modified = True
    return redirect(url_for('chat'))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
