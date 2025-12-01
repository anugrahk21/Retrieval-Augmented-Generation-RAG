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


#Configure Google Gemini API client
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
MODEL_NAME="gemini-2.5-flash-lite"

class GeminiAPI:
    def __init__(self, api_key: Optional[str]=None):
        self.api_key=api_key or GEMINI_API_KEY
    
    def generate_response(self, model:str, content:list, system_instruction:str) -> str:
        try:
            client=genai.Client(api_key=self.api_key)
            config=genai.types.GenerateContentConfig(system_instruction=system_instruction)
            response=client.models.generate_content(model=model, content=content, config=config)
            
        except APIError as e:
            st.error(f"API Error: {e}")
            return f"API Error: {e}"
        
        except Exception as e:
            st.error(f"Unexpected Error: {e}")
            return f"Unexpected Error: {e}"


#Streamlit App UI
st.set_page_config(page_title="RAG with Google Gemini", layout="wide")
st.title("Retrieval-Augmented Generation (RAG) with Google Gemini")
st.markdown("""
This application demonstrates Retrieval-Augmented Generation (RAG) using Google Gemini.
Upload a document, and the LLM is forced to answer  *only* by referencing the document content in its response.

Supported file types: `.txt`, `.md`, `.pdf`, `.docx`
""")

