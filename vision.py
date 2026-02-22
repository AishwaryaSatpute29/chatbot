# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Image Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

st.markdown(
    """
    <style>
        body {
            background-color: gray;
            color: #333;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
            padding-top: 20px;
            padding-bottom: 20px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stFileUploader, .stButton {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .stTextInput input, .stFileUploader input, .stButton button {
            border-radius: 8px;
        }
        .stButton button {
            background-color: #28a745;
            color: #fff;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #218838;
        }
    </style>
    """,
    unsafe_allow_html=True
)    