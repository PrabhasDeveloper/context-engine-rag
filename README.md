# Context Engine RAG

A production-style Retrieval-Augmented Generation (RAG) learning project built from scratch while learning RAG engineering concepts.

## Project Goal

Build a complete RAG pipeline step by step:

* PDF Ingestion
* Chunking (multiple strategies)
* Embeddings
* Vector Database
* Retrieval
* LLM Generation

## Tech Stack

* Python
* LangChain
* PyPDFLoader
* LangChain Text Splitters
* FAISS (coming later)
* Sentence Transformers (coming later)

## Project Structure

```text
context-engine-rag/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── sample.pdf
└── src/
    ├── ingestion.py
    └── chunking.py
```

## Current Progress

* [x] PDF Ingestion
* [x] Fixed Size Chunking
* [x] Recursive Chunking
* [ ] Token-Based Chunking
* [ ] Semantic Chunking
* [ ] Structure-Based Chunking
* [ ] Parent–Child Chunking
* [ ] Embeddings
* [ ] Vector Database
* [ ] Retrieval
* [ ] Chatbot

## Learning Notes

This repository is built incrementally, with each RAG stage implemented and committed separately to demonstrate the complete engineering workflow.
