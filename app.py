from src.ingestion import load_pdf
from src.chunking import fixed_chunking

documents = load_pdf("data/sample.pdf")

chunks = fixed_chunking(documents)

print(f"Total Chunks: {len(chunks)}")

print(f"Total Chunks Created: {len(chunks)}")
print("=" * 70)

for i, chunk in enumerate(chunks):
    print(f"\nChunk ID: {i}")
    print(f"PDF Page: {chunk.metadata['page'] + 1}")
    print(f"Source: {chunk.metadata['source']}")
    print("-" * 40)
    print(chunk.page_content[:200])   # Preview first 200 characters
    print("=" * 70)