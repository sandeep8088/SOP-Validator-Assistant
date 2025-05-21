import streamlit as st
import openai
import os

st.title("SOP Validator")

openai.api_key = os.getenv("OPENAI_API_KEY")

sop_text = st.text_area("Paste your SOP document content")

if sop_text:
    prompt = f"Check this SOP for outdated steps, redundancies, or inconsistencies and suggest improvements:\n\n{sop_text}"
    with st.spinner("Validating SOP..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message["content"])
