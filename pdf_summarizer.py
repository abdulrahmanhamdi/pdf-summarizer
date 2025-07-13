import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

st.title("PDF Summarizer")
st.markdown("Upload a PDF file and get a short summary using NLP.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        pdf_text += page.get_text()
    doc.close()

    st.subheader("Extracted Text")
    st.text_area("Full Text", pdf_text[:2000] + "...", height=200)

    if st.button("Summarize"):
        with st.spinner("Summarizing... please wait."):

            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

            chunk_size = 1000
            chunks = [pdf_text[i:i+chunk_size] for i in range(0, len(pdf_text), chunk_size)]

            summaries = []
            for chunk in chunks:
                if len(chunk.strip()) > 0:
                    try:
                        result = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
                        summaries.append(result[0]['summary_text'])
                    except Exception as e:
                        summaries.append("[Error in the Summary : {}]".format(str(e)))

            full_summary = "\n\n".join(summaries)
            st.subheader("📌 Summary")
            st.success(full_summary)
