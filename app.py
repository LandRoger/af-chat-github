import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

st.title("Chatbot Application by AgileFever with OpenAI API")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

question = st.text_input("Ask a question to the chatbot:")

if question:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=question
    )
    st.write("Chatbot's answer:", response.output_text)