# 🚀 Retrieval-Augmented Generation (RAG) with Google Gemini

A powerful Streamlit application that demonstrates Retrieval-Augmented Generation (RAG) using Google's Gemini AI. Upload your documents and ask questions - the AI will answer based *solely* on the document content!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Why RAG? Understanding Different Approaches](#why-rag-understanding-different-approaches)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported File Types](#supported-file-types)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Questions & Troubleshooting](#questions--troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

This application implements a Retrieval-Augmented Generation (RAG) system that:
- Allows users to upload documents (TXT, MD, PDF, DOCX)
- Processes and extracts content from uploaded documents
- Uses Google Gemini AI to answer questions based exclusively on document content
- Provides clear responses when information isn't available in the document

## 🧠 Why RAG? Understanding Different Approaches

When working with Large Language Models (LLMs), there are three main approaches to customize their responses to your specific data. Understanding the differences is crucial for choosing the right solution.

### 📝 Normal Prompting

**What it is:** Simply asking the LLM a question using its pre-trained knowledge.

```
User: "What are the key findings in the 2024 financial report?"
LLM: "I don't have access to your specific 2024 financial report..."
```

**Pros:**
- ✅ Instant - no setup required
- ✅ Free (just API costs)
- ✅ Works for general knowledge questions

**Cons:**
- ❌ No access to your private/recent documents
- ❌ Can't answer company-specific questions
- ❌ Knowledge cutoff date limits
- ❌ May hallucinate when it doesn't know

**Best for:** General questions, public knowledge, creative tasks

---

### 🔍 RAG (Retrieval-Augmented Generation) ⭐ *This Project*

**What it is:** Dynamically providing your document content to the LLM along with your question, forcing it to answer from that specific context.

```
System: "Here's the document content: [Full 2024 Report]"
User: "What are the key findings?"
LLM: "Based on the provided document, the key findings are: 1. Revenue increased by 23%..."
```

**Pros:**
- ✅ Works with your private/proprietary documents
- ✅ Always up-to-date (uses latest document version)
- ✅ No retraining needed - instant updates
- ✅ Cost-effective - pay only for API calls
- ✅ Can cite specific sections from documents
- ✅ Maintains model's general capabilities
- ✅ Easy to implement and modify

**Cons:**
- ❌ Token limits restrict document size
- ❌ Sends data to external API (privacy concern)
- ❌ Requires document parsing infrastructure
- ❌ Slightly slower than normal prompting

**Best for:** Document Q&A, internal knowledge bases, research papers, legal documents, customer support with documentation

---

### 🎓 Fine-Tuning

**What it is:** Retraining the model on your specific dataset to permanently alter its behavior and knowledge.

```
Training Data: 10,000 examples of your company's style and information
Result: Model now "knows" your company's data intrinsically
```

**Pros:**
- ✅ Model learns your specific domain/style deeply
- ✅ No need to send documents with every request
- ✅ Faster responses (no document processing)
- ✅ Better for specific tasks/formats
- ✅ Can work offline (if self-hosted)

**Cons:**
- ❌ Expensive (training costs thousands of dollars)
- ❌ Time-consuming (days to weeks)
- ❌ Requires large dataset (1000s of examples)
- ❌ Needs ML expertise
- ❌ Difficult to update (requires retraining)
- ❌ Risk of forgetting general knowledge
- ❌ Can still hallucinate

**Best for:** Specific writing styles, domain-specific language, repetitive specialized tasks

---

### 📊 Comparison Table

| Feature | Normal Prompting | RAG (This Project) | Fine-Tuning |
|---------|------------------|-------------------|-------------|
| **Setup Time** | Instant | Minutes | Days/Weeks |
| **Cost** | $ (API only) | $$ (API + storage) | $$$$ (Training + API) |
| **Private Data** | ❌ No | ✅ Yes | ✅ Yes |
| **Real-time Updates** | N/A | ✅ Instant | ❌ Requires retraining |
| **Accuracy on Docs** | ⭐ Low | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐⭐ High |
| **Token Usage** | Low | High | Low |
| **Expertise Required** | None | Basic | Advanced ML |
| **Best Use Case** | General Q&A | Document-based Q&A | Task specialization |

---

### 🎯 Why This Project Uses RAG

RAG is the perfect middle ground for most document-based applications:

1. **No Training Required**: Upload a document and start querying immediately
2. **Always Current**: Update your document, and responses update instantly
3. **Cost-Effective**: No expensive training runs
4. **Transparent**: You can see exactly what content the AI is using
5. **Flexible**: Works with any document type (PDF, DOCX, TXT, MD)
6. **Scalable**: Easy to add new documents or change content

**Real-World Example:**
- ❌ Normal Prompting: "What's in the contract?" → AI doesn't know
- ✅ RAG: Upload contract → "What's in the contract?" → AI reads and answers
- 🎓 Fine-Tuning: Would require training on thousands of contracts (overkill!)

## ✨ Features

- **📄 Multi-Format Support**: Upload `.txt`, `.md`, `.pdf`, or `.docx` files
- **🤖 AI-Powered Q&A**: Leverages Google Gemini 2.5 Flash Lite model
- **🔒 Document-Constrained Responses**: AI answers only from uploaded document content
- **👁️ Document Preview**: View uploaded document content before querying
- **⚡ Real-Time Processing**: Fast document parsing and response generation
- **🎨 Clean UI**: Intuitive Streamlit interface with modern design
- **🔐 Secure**: API keys managed through environment variables

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Step 1: Clone the Repository

```bash
git clone https://github.com/anugrahk21/Retrieval-Augmented-Generation-RAG.git
cd Retrieval-Augmented-Generation-RAG
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies



```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

**Important**: Never commit your `.env` file to version control!

## 🚀 Usage

### Running the Application

```bash
streamlit run RAD.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Upload Document**: Click "Browse files" and select a document (TXT, MD, PDF, or DOCX)
2. **Preview Content**: Optionally expand "View Document Content" to see what was uploaded
3. **Ask Question**: Enter your question in the text area
4. **Generate Response**: Click "Generate RAG Response" button
5. **View Answer**: The AI-generated answer will appear in the RAG Response section

### Example Questions

- "What is the main topic of this document?"
- "Summarize the key findings in under 100 words"
- "What are the conclusions mentioned?"
- "List all the recommendations provided"

## 📁 Supported File Types

| Format | Extension | Library Used |
|--------|-----------|--------------|
| Text | `.txt` | Built-in Python |
| Markdown | `.md` | Built-in Python |
| PDF | `.pdf` | PyPDF2 |
| Word Document | `.docx` | python-docx |

## 🔍 How It Works

### RAG Pipeline

1. **Document Upload**: User uploads a document through the Streamlit interface
2. **Content Extraction**: The app extracts text content based on file type:
   - Text/Markdown: Direct UTF-8 decoding
   - PDF: Page-by-page text extraction using PyPDF2
   - DOCX: Paragraph-by-paragraph extraction using python-docx
3. **Question Input**: User enters a natural language question
4. **Prompt Construction**: The system creates a combined prompt with:
   - Document content
   - User's question
   - System instruction to answer only from the document
5. **AI Processing**: Google Gemini processes the prompt and generates a response
6. **Response Display**: Answer is displayed with proper formatting

### System Architecture

```
User Upload → Document Parser → Content Extraction
                                      ↓
User Question → Prompt Builder ← Document Content
                    ↓
              Gemini API (with System Instruction)
                    ↓
              Response Formatter → Display Answer
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

### Model Configuration

You can change the model in `RAD.py`:

```python
MODEL_NAME="gemini-2.5-flash-lite"  # Default model
```

Available models:
- `gemini-2.5-flash-lite` (faster, less expensive)
- `gemini-2.5-flash` (balanced)
- `gemini-pro` (most capable)

## ❓ Questions & Troubleshooting

### Common Questions

**Q: Where do I get a Gemini API key?**  
A: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) to generate a free API key.

**Q: What's the maximum document size?**  
A: While there's no hard limit in the app, the Gemini API has token limits. For best results, keep documents under 50,000 words.

**Q: Can I use this with private/sensitive documents?**  
A: The documents are sent to Google's Gemini API. Review Google's [privacy policy](https://policies.google.com/privacy) before uploading sensitive information.

**Q: Why does it say "PDF reading functionality is not available"?**  
A: Install PyPDF2: `pip install PyPDF2`

**Q: Why does it say "DOCX reading functionality is not available"?**  
A: Install python-docx: `pip install python-docx`

**Q: Can the AI access information from the internet?**  
A: No. The system instruction explicitly tells the AI to answer only from the uploaded document content.

### Common Errors

**Error: `APIError: Invalid API key`**  
- Solution: Check that your `GEMINI_API_KEY` in `.env` is correct and active

**Error: `ModuleNotFoundError: No module named 'dotenv'`**  
- Solution: `pip install python-dotenv`

**Error: `Unexpected Error: 'NoneType' object has no attribute 'text'`**  
- Solution: Check your internet connection and API key. The Gemini API might be unavailable.

**Error: Document content appears empty**  
- Solution: Ensure the document contains extractable text (not just images)

**Error: `streamlit: command not found`**  
- Solution: Ensure Streamlit is installed: `pip install streamlit`

### Performance Issues

**Slow response times?**
- Large documents take longer to process
- Consider using a faster model like `gemini-2.5-flash-lite`
- Check your internet connection speed

**App crashes on large PDFs?**
- Some PDFs with complex formatting may cause issues
- Try converting to TXT or DOCX format first
- Split large documents into smaller sections

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add support for more file formats (e.g., CSV, Excel, HTML)
- Implement document chunking for very large files
- Add conversation history/chat interface
- Create unit tests
- Improve error handling and user feedback
- Add document preprocessing options

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Contact

**Anugrah K.**

- GitHub: [@anugrahk21](https://github.com/anugrahk21)
- LinkedIn: [anugrah-k](https://www.linkedin.com/in/anugrah-k/)
- Email: anugrah.k910@gmail.com

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) for the powerful AI model
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing
- [python-docx](https://python-docx.readthedocs.io/) for DOCX processing

---

⭐ If you found this project helpful, please give it a star!

**Made with ❤️ by Anugrah K.**