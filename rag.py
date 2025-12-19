from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from pathlib import Path

def load_pdf_rag(data_dir="data"):
    data_dir = Path(data_dir)

    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir.resolve()}")

    pdf_files = list(data_dir.glob("*.pdf"))

    if not pdf_files:
        raise ValueError(f"No PDF files found in {data_dir.resolve()}")

    all_docs = []

    for pdf in pdf_files:
        print(f"📄 Loading: {pdf.name}")
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        # Add source metadata
        for doc in docs:
            doc.metadata["source"] = pdf.name

        all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(all_docs)

    embeddings = OllamaEmbeddings(model="llama3.2")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vectorstore.as_retriever(search_kwargs={"k": 3})
