from dotenv import load_dotenv
load_dotenv()

import gradio as gr
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    # Concatenate streamed chunks into a single string
    full_response = ''.join([chunk.text for chunk in response])
    return full_response

chat_history = []

def chat_interface(user_input):
    global chat_history
    if user_input:
        response = get_gemini_response(user_input)
        chat_history.append(f"You: {user_input}")
        chat_history.append(f"Bot: {response}")
        # Display chat history with newlines
        chat_display = "\n".join(chat_history)
        return chat_display

iface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Mental Health Support Chatbot",
    description="A Gradio-powered chatbot using Google's Gemini Pro model.",
)

iface.launch()
