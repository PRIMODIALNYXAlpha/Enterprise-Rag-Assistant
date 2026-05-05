# 🤖 Enterprise RAG Assistant (Multi-PDF AI Chatbot)

## 📌 Overview

This project is an **Enterprise-level AI Knowledge Assistant** that allows users to interact with multiple PDF documents using a chatbot interface.

It uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers instead of simple keyword matching.

---

## 🚀 Key Features

* 📄 Multi-PDF upload and processing
* 💬 ChatGPT-like conversational interface
* 🧠 Context-aware answers using RAG
* ⚡ Fast inference using Groq API
* 🔍 Semantic search with embeddings
* 📊 Clean Streamlit UI

---

## 🧠 How It Works

```text
User Query
   ↓
Embedding Model
   ↓
Vector Store (FAISS)
   ↓
Retrieve Relevant Chunks
   ↓
LLM (Groq - LLaMA)
   ↓
Generated Answer
```

---

## 🏗️ Project Structure

```text
Enterprise-RAG-Assistant/
│
├── app.py
├── requirements.txt
├── .env                # API key (not pushed)
│
├── chains/
│   └── chat_chain.py
│
├── services/
│   ├── llm_service.py
│   └── vector_store.py
│
├── utils/
│   └── pdf_loader.py
│
├── data/               # Uploaded PDFs
└── OutPuts/            # Screenshots
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/PRIMODIALNYXAlpha/Enterprise-Rag-Assistant.git
cd Enterprise-Rag-Assistant
```

---

### 🔹 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Add API Key

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

---

### 🔹 5. Run Application

```bash
streamlit run app.py
```

---

## 🌐 Usage

1. Select mode:

   * LLM Only
   * Single PDF
   * Multiple PDFs

2. Upload PDF(s)

3. Ask questions like:

   * "Summarize this document"
   * "Explain machine learning"
   * "What is the conclusion?"

---

## 🧠 Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* Sentence Transformers
* Groq API

---

## 🔍 Core Concepts

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Document Chunking
* LLM Integration

---

## ⚠️ Notes

* `.env` file is excluded for security
* Large PDF files are not uploaded to GitHub
* Requires internet for API calls

---

## 🚀 Future Improvements

* 💬 Chat memory (conversation history)
* 🌐 Deployment (Streamlit Cloud / AWS)
* 📊 Better UI/UX
* 🔐 User authentication
* 📄 Source highlighting

---

## 👨‍💻 Author

**Tarun SR**

---

## ⭐ Conclusion

This project demonstrates how modern AI systems combine:

* LLMs
* Vector databases
* Semantic search

to build intelligent document assistants used in real-world enterprise applications.

---

⭐ *If you found this useful, consider starring the repo!*
