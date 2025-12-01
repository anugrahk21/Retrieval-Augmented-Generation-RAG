#Retrieval-Augmented Generation (RAG)

import streamlit as st # For building web apps requests 
import os # For environment variable management requests
from typing import Optional # For type hinting
from io import BytesIO # For handling byte streams
from google import genai # Google Gemini API client library
from google.genai.errors import APIError # For handling API errors

try:
    from pdf import pdfreader

except ImportError:
    pdfreader=None

try:
    from docx import Document

except ImportError:
    Document=None

# Function to read content from uploaded document
def read_document_content(uploaded_file):
    file_extension=os.path.splitext(uploaded_file.name)[1].lower()

    try:
        if file_extension in ['.txt', '.md']:
            return uploaded_file.read().decode('utf-8')
        
        elif file_extension == '.pdf':
            if not pdfreader:
                st.error("PDF reading functionality is not available. Please install the required library.")
                return f"PDF reading functionality is not available. Please install the required library."
            reader=pdfreader(uploaded_file)
            text=""
            for page in reader.pages:
                text+=page.extract_text() or "" # Extract text from each page
            return text

        elif file_extension == '.docx':
            if not Document:
                st.error("DOCX reading functionality is not available. Please install the required library.")
                return f"DOCX reading functionality is not available. Please install the required library."
            doc=Document(BytesIO(uploaded_file.getvalue()))
            text="\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text

    except Exception as e:
        st.error(f"Error reading document: {e}")
        return f"Error reading document: {e}"
