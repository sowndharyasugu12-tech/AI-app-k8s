import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.title("Devops AI agent")
query = st.text_area("Ask something related to AI and DevOps..")

if st.button("Run Agent"):
    with st.spinner("Thinking..."):
        response = model.generate_content(query)
        st.write(response.text)

