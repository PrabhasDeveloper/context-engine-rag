from src.ingestion import load_pdf
from src.chunking import recursive_chunking

documents = load_pdf("data/sample.pdf")

chunks = recursive_chunking(documents)

print(f"Total Recursive Chunks: {len(chunks)}")

for chunk in chunks[:5]:
    print("=" * 60)
    print(f"Chunk ID : {chunk.metadata['chunk_id']}")
    print(f"Page     : {chunk.metadata['page'] + 1}")
    print(chunk.page_content[:250])