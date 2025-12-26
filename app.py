import streamlit as st
from crawler import validate_url, crawl
from content_extractor import clean_content
from module_inferencer import infer_modules
from output_formatter import format_output

st.title("Pulse - Module Extraction AI Agent")

url = st.text_input("Enter documentation URL:")
if st.button("Extract"):
    if validate_url(url):
        pages = crawl(url)
        cleaned = [clean_content(p) for p in pages]
        modules = infer_modules(cleaned)
        output = format_output(modules)
        st.json(output)
        st.download_button("Download JSON", str(output), "modules.json")
    else:
        st.error("Invalid or unreachable URL")
