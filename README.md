# 🤖 Customer Support Assistant (RAG System)

## 📌 Overview
This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant designed to answer user queries using a knowledge base.

The system retrieves relevant information from stored documents and provides accurate, context-aware responses through a simple web interface.

This project was developed as part of an internship to demonstrate practical understanding of RAG systems and AI-based workflows.

---

## 🚀 Features
- 📄 Knowledge-based question answering  
- 🔍 Semantic search using embeddings  
- 🧠 Context-aware responses  
- ⚡ Fast retrieval using vector database  
- 🌐 Clean and simple Streamlit UI  
- 🔄 Modular and scalable pipeline  

---

## 🧠 How It Works

1. Knowledge data is loaded from a document (TXT/PDF)
2. Data is split into smaller chunks
3. Chunks are converted into vector embeddings
4. Stored in ChromaDB (vector database)
5. User query is processed
6. Relevant chunks are retrieved
7. Final response is generated and displayed

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Vector Database:** ChromaDB  
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2)  
- **Framework:** LangChain  

---

## 📂 Project Structure

```
rag-customer-support-assistant/
│
├── app.py
├── rag_pipeline.py
├── langgraph_pipeline.py
├── requirements.txt
├── README.md
│
├── data/
│   └── knowledge.txt / knowledge.pdf
│
└── docs/
    ├── HLD.pdf
    ├── LLD.pdf
    └── Technical_Documentation.pdf
```

---

## ▶️ How to Run

1. Clone the repository:

git clone https://github.com/your-username/rag-customer-support-assistant.git

cd rag-customer-support-assistant


2. Install dependencies:

pip install -r requirements.txt


3. Run the application:

streamlit run app.py


---

## 💡 Sample Queries

- refund policy  
- order tracking  
- contact support  
- password reset  

---

## 📘 Notes

- The system currently uses `.txt` for simplicity.
- It can be extended to support PDF documents using `PyPDFLoader`.

---

## 📊 Future Enhancements

- Multi-document support  
- Improved retrieval accuracy  
- Feedback-based learning  
- Chat history memory  
- Cloud deployment  

---

## 🎯 Conclusion

This project demonstrates the implementation of a real-world RAG system using embeddings, vector search, and a simple UI. It highlights how AI can be used to automate customer support efficiently.

---

## 👤 Author

**Srinidhi Kasam**  
