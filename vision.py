from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from PIL import Image
import google.generativeai as genai
import io

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(user_input, image):
    model = genai.GenerativeModel('gemini-pro-vision')

    # Convert image from Gradio format to PIL Image
    if image is not None:
        image = Image.open(io.BytesIO(image))

    if user_input != "":
        response = model.generate_content([user_input, image])
    else:
        response = model.generate_content(image)
    return response.text

def chat_interface(user_input, image):
    if user_input or image:
        response = get_gemini_response(user_input, image)
        return response

iface = gr.Interface(
    fn=chat_interface,
    inputs=[
        gr.Textbox(lines=2, placeholder="Type your message here..."),
        gr.Image(type="pil")
    ],
    outputs="text",
    title="Mental Health Support Chatbot",
    description="A Gradio-powered chatbot using Google's Gemini Pro Vision model.",
)

iface.launch()
