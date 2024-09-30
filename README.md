# Gemini AI Chatbot

This is a simple chatbot implementation using Google's `google.generativeai` (Gemini) API. The bot allows users to chat with an AI model via the command line, generating natural language responses in real time.

## Features
- Command-line interface for interacting with the AI.
- Uses Google Generative AI (`gemini-1.5-flash`) for response generation.
- Configurable parameters like `temperature`, `top_p`, and `top_k` for tuning response generation.

## Prerequisites
- Python 3.x
- A valid Google Gemini API key.

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/gemini-ai-chatbot.git
cd gemini-ai-chatbot
```

### 2.  Install dependencies
- Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
- In python script (`main.py`),replace `"ADD_GEMINI _KEY"` with your actual Gemini API key"
```bash
api_key = "your_actual_api_key_here"
```
### 4. Run the chatbot
-To start the chatbot,run:
```bash
python gemini_chatbot.py
```
