#AIzaSyANynujtXPe7jgkHqCF8K-ckvFc_wqEVCA
from dotenv import load_dotenv
load_dotenv()

import gradio as gr
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyANynujtXPe7jgkHqCF8K-ckvFc_wqEVCA"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def chat_interface(user_input):
    if user_input:
        response = get_gemini_response(user_input)
        return response

iface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Mental Health Support Chatbot",
    description="A Gradio-powered chatbot using Google's Gemini Pro model.",
)

iface.launch()
