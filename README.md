# rag_agent2_multi_pdf_reader


# 📄 Multi-Document RAG Chatbot using LLaMA 3 (Local)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that can answer questions from **multiple research PDFs** using a **locally hosted LLaMA 3 model**.
It combines **semantic search** with **LLM reasoning** to produce accurate, document-grounded responses through a **Streamlit web interface**.

---

## 🚀 What This Project Does

* Ingests **multiple PDF documents** (research papers & documentation)
* Splits documents into semantic chunks
* Generates embeddings using a **local embedding model**
* Stores and retrieves vectors using **ChromaDB**
* Uses **LLaMA 3 (via Ollama)** to generate answers based on retrieved context
* Provides an **interactive Streamlit UI** for querying documents

---

## 🧠 Architecture Overview

```
User Query
   ↓
Streamlit UI
   ↓
Retriever (ChromaDB + Embeddings)
   ↓
Relevant PDF Chunks
   ↓
LLaMA 3 (Ollama)
   ↓
Final Answer
```

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Ollama (LLaMA 3)**
* **nomic-embed-text** (Embeddings)
* **ChromaDB** (Vector Database)
* **Streamlit**
* **PyPDF**

---

## 📂 Project Structure

```
new_rag/
├── app.py            # Streamlit UI
├── rag.py            # Multi-PDF RAG pipeline
├── llm.py            # LLaMA 3 + conversation memory
├── data/             # PDF documents
│   ├── attention_is_all_you_need.pdf
│   ├── bert_research.pdf
│   ├── rag_research.pdf
│   └── welcome_langchain.pdf
├── chroma_db/        # Persistent vector store
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Ollama Models

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 💡 Example Queries

* “Explain the attention mechanism”
* “What is RAG and how does it work?”
* “How is BERT different from GPT?”
* “Summarize the research papers”
* “How does LangChain help with LLM orchestration?”

---

## 🌟 Why This Project Matters

This project demonstrates:

* **End-to-end RAG pipeline design**
* **Multi-document knowledge ingestion**
* **Local LLM deployment (no API costs)**
* **Practical use of vector databases**
* **Production-style AI application structure**

It goes beyond simple chatbots by ensuring **answers are grounded in real documents**.

---

## 🔮 Future Enhancements

* Source citations (PDF + page number)
* PDF upload through UI
* Multi-agent RAG workflows
* Dockerized deployment
* Cloud-based LLM toggle

---

