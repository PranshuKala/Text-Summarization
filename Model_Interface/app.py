import os
import re
import torch
import streamlit as st
from summa import summarizer
import nltk
from nltk.corpus import stopwords
from simpletransformers.t5 import T5Model, T5Args

# Set the page configuration
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="wide")

# Download NLTK stopwords
nltk.download("stopwords")

# Load stopwords once
stop = set(stopwords.words('english'))

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'model_summarize_abstractive')
    model = T5Model('t5', model_path, use_cuda=False)
    return model

model = load_model()

def generate_extractive_summary(text):
    text = ' '.join([word for word in text.split() if word not in stop])
    extractive_sum = summarizer.summarize(text, ratio=0.5, language='english')
    return extractive_sum

def summarize_text(text):
    summary = model.predict([text])[0]
    return summary

# Streamlit App
st.title("Text Summarizer")
st.markdown("""
<style>
body {
    color: #2E2E2E;
    background-color: #2B3033;
}
.stTextArea {
    background-color: #2B3033;
    color: white;
    border: 1px solid #2E2E2E;
    border-radius: 5px;
}
.stButton>button {
    color: white;
    background-color: #007BFF;
    border: none;
    border-radius: 5px;
}
.stButton>button:hover {
    background-color: #0056b3;
}
footer {
    text-align: center;
    padding: 10px 0;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

st.header("Enter your Text ")

text_input = st.text_area("text", height=200, label_visibility="collapsed")

def copy_to_clipboard(summary):
    js = f"""navigator.clipboard.writeText(`{summary}`)"""
    return f'<script>{js}</script>'

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Abstractive Summary"):
        if text_input.strip() == "":
            st.error("Please enter some text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                summary_output = summarize_text(text_input)
                st.subheader("Abstractive Summary")
                st.write(summary_output)
                st.markdown(f"<button onclick=\"{copy_to_clipboard(summary_output)}\">Copy to clipboard</button>", unsafe_allow_html=True)

with col2:
    if st.button("Generate Extractive Summary"):
        if text_input.strip() == "":
            st.error("Please enter some text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                summary_output = generate_extractive_summary(text_input)
                st.subheader("Extractive Summary")
                st.write(summary_output)
                st.markdown(f"<button onclick=\"{copy_to_clipboard(summary_output)}\">Copy to clipboard</button>", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer>
    <hr>
    <p>Text Summarization App</p>
</footer>
""", unsafe_allow_html=True)
