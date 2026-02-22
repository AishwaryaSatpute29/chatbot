from dotenv import load_dotenv
load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini Pro Fast API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize session state for chat history and user feedback
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'user_feedback' not in st.session_state:
    st.session_state['user_feedback'] = []

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Text Application")

# User input
input_question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input_question:
    # Get Gemini response
    response = get_gemini_response(input_question)

    # Add user query and response to chat history
    st.session_state['chat_history'].append(("You", input_question))
    st.subheader("The Response is")
    
    # Display Gemini's response
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

    # Ask for user feedback
    feedback = st.radio("Was the response helpful?", ("Yes", "No"))
    st.session_state['user_feedback'].append(feedback)

# Display chat history and user feedback
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

# Display user feedback
st.subheader("User Feedback")
for feedback in st.session_state['user_feedback']:
    st.write(f"User Feedback: {feedback}")

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
            padding-top: 30px;
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












