
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ API key not found. Please check your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Page config
st.set_page_config(
    page_title="Gemini AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Gemini AI Chat App")
st.write("Ask anything and get AI-powered responses!")

# Input box
user_prompt = st.text_area("Enter your prompt:", height=120)

# Button
if st.button("Generate Response"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            response = model.generate_content(user_prompt)

            st.success("Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
