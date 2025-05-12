# **Gemini Fine Tuning Chatbot Using PDF**

The Gemini Fine Tuning Chatbot Using PDF is a Flask-based AI assistant that extracts and provides answers strictly from a given PDF document. This chatbot uses Google's Gemini AI model to process queries and return precise responses based on the document’s content.

![Demo Screenshot](https://github.com/Eya-Laouini/Gemini-Fine-Tuning/blob/main/gemini-chatbot-demo.png)

## Features

- Extracts and retrieves information exclusively from a provided PDF file.
- Real-time AI-powered responses based on document content.
- Session-based chat history management.
- Flask web interface for seamless interaction.

## Installation

To set up the Gemini PDF Chatbot, you need to have Python installed on your system.

### **1. Clone the repository:**
```bash
git clone https://github.com/Eya-Laouini/Gemini-RAG
cd Gemini-RAG
```

### **2. Set up a virtual environment (optional but recommended):**
```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate    # On Windows
```

### **3. Install dependencies:**
```bash
pip install -r requirements.txt
```

### **4. Set up your Gemini API Key:**
Obtain a Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey) and set it as an environment variable:
```bash
export GEMINI_API_KEY=your_api_key_here  # On macOS/Linux
set GEMINI_API_KEY=your_api_key_here    # On Windows
```

### **5. Add your PDF document:**
Place the PDF file in the project directory and update the `PDF_FILE_PATH` variable in `gemini_fine_tuned.py` to match your file name.

### **6. Run the application:**
```bash
python gemini_fine_tuned.py
```
After starting the app, open your browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Customization
You can modify the chatbot's behavior, UI, and PDF processing logic by editing `gemini_fine_tuned.py` and updating the HTML/CSS files in the `templates` folder.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.
