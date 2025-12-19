import streamlit as st
from llm import load_llm_with_memory
from rag import load_pdf_rag

st.set_page_config(page_title="AI Chatbot with RAG", layout="centered")
st.title("🧠 AI Assistant (Memory + PDF RAG)")

chain = load_llm_with_memory()
retriever = load_pdf_rag("dataqui")

query = st.text_input("Ask a question")

if query:
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([d.page_content for d in docs])

    response = chain.predict(
        input=f"Context:\n{context}\n\nQuestion: {query}"
    )

    st.write("### 🤖 Answer")
    st.write(response)
