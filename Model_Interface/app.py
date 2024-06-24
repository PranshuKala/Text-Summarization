from simpletransformers.t5 import T5Model, T5Args
import torch

pred_params = {
    'max_seq_length': 512,
    'use_multiprocessed_decoding': False
}

# Check if CUDA is available
cuda = torch.cuda.is_available()

# Load the model
model_path = 'C:/Users/Perplex420/Desktop/Text_Summarization/Model_Interface/model_summarize_abstractive'

model = T5Model('t5', model_path, args=pred_params, use_cuda=cuda)


import streamlit as st


def summarize_text(text):
    summary = model.predict([text])[0]
    return summary

st.set_page_config(page_title="Text Summarization", page_icon="📝", layout="wide")
st.title("Text Summarization")
st.markdown("""
<style>
body {
    color: #2E2E2E;
    background-color: #F5F5F5;
}
</style>
""", unsafe_allow_html=True)

st.header("Enter the text you want to summarize")

text_input = st.text_area("Text Input", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.error("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary_output = summarize_text(text_input)
            st.subheader("Summary")
            st.write(summary_output)

# Footer
st.markdown("""
<footer style='text-align: center; padding: 10px 0; color: #555;'>
    <hr>
    <p></p>
</footer>
""", unsafe_allow_html=True)