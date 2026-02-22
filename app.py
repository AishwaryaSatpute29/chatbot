from dotenv import load_dotenv
import streamlit as st
import os
import textwrap

import google.generativeai as genai

from IPython.display import Markdown

# Load environment variables
load_dotenv()

# Configure Google API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to convert text to Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to get Gemini response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Set Streamlit page configuration
st.set_page_config(
    page_title="Q&A Demo",
    page_icon=":rocket:",
    layout="centered",  # Center content on the page
)

# Header and introduction with colorful text
st.title(":gem: Gemini LLM Text Application")
st.write("Welcome to the Gemini Language Model Application. Ask a question and get a response!")

# Input box for user question with a colorful background
input_question = st.text_input("Input: ", key="input", help="Type your question here.")

# Ask button with a vibrant color and rounded corners
submit_button = st.button("Ask the question", key="submit_button")

# Display response with a colorful subheader
if submit_button:
    response = get_gemini_response(input_question)
    st.subheader("The Response is :")
    st.write(response)
    st.success("Question successfully answered!")

# Custom footer with a different color and box shadow
st.markdown("---", unsafe_allow_html=True)
st.write("Developed by Aishwarya Satpute")

# Additional styling with vibrant colors, rounded corners, and improved borders
st.markdown(
    """
    <style>
        body {
            color: #333;
            background-color: gray;
            border-top: 8px solid #3498db;
            
            border-bottom: 8px solid #3498db;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
            border-radius: 12px;
            margin-top:10px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stTextInput, .stButton {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .stTextInput input {
            border-radius: 8px;
        }
        .stButton button {
            background-color: #28a745;
            color: #fff;
            border-radius: 8px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #218838;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)