import os
import google.generativeai as genai

# Fetch API key from environment variable GEMINI_API_KEY
api_key = "ADD_GEMINI_API_KEY"
if not api_key:
    raise ValueError("API key is missing. Set GEMINI_API_KEY environment variable.")

# Configure the API with the API key
genai.configure(api_key=api_key)

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    generation_config=generation_config
)

chat_session = model.start_chat(
    history=[
    ]
)
while True:
    usr = input("You : ").lower()
    if usr == "exit":
        break
    else:
        response = chat_session.send_message(usr)
        print("AI : ",response.text)
