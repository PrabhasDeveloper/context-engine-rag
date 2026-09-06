from langchain_community.document_loaders import PyPDFLoader

# src/chunking.py

from langchain_core.documents import Document


def fixed_chunking(documents, chunk_size=500, chunk_overlap=50):
    """
    Split each Document into fixed-size chunks while preserving metadata.
    """

    chunks = []
    chunk_id = 0 

    for doc in documents:

        text = doc.page_content
        metadata = doc.metadata.copy()

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_id"] = chunk_id

            chunks.append(
                Document(
                    page_content=chunk_text,
                    metadata=metadata
                )
            )

            chunk_id += 1   

            start += chunk_size - chunk_overlap

    return chunks