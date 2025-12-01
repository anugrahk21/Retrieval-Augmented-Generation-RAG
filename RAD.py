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



