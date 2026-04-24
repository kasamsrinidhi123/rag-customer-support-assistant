# rag_pipeline.py

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


# -------------------------------
# BUILD RAG SYSTEM (PDF)
# -------------------------------
def build_rag():
    # Load PDF
    loader = PyPDFLoader("data/knowledge.pdf")
    pages = loader.load()

    # Convert PDF pages into smaller lines (better retrieval)
    docs = []
    for page in pages:
        lines = page.page_content.split("\n")
        for line in lines:
            if line.strip():
                docs.append(Document(page_content=line.strip()))

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Vector DB
    db = Chroma.from_documents(docs, embeddings)

    # Retriever
    retriever = db.as_retriever(search_kwargs={"k": 5})

    return retriever


# Initialize
retriever = build_rag()


# -------------------------------
# SMART RETRIEVE (SAME LOGIC)
# -------------------------------
def retrieve_docs(query: str) -> str:
    docs = retriever.invoke(query)

    if not docs:
        return ""

    query_words = query.lower().split()
    filtered = []

    for doc in docs:
        content = doc.page_content.lower()

        # Keep only relevant chunks
        if any(word in content for word in query_words):
            filtered.append(doc.page_content)

    # If nothing matched → HITL trigger
    if not filtered:
        return ""

    # Return best 1–2 results only
    return "\n".join(filtered[:2])