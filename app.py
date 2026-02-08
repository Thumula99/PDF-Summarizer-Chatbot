import streamlit as st
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text

st.title("PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    if st.button("Summarize"):
        with st.spinner("Working..."):
            text = extract_text_from_pdf(uploaded_file)
            summary = summarize_text(text)

        st.subheader("Summary")
        st.write(summary)
