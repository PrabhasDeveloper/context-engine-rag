from src.ingestion import load_pdf
from src.chunking import (
    fixed_chunking,
    recursive_chunking,
    token_chunking,
)

# --------------------------------------------------
# SELECT CHUNKING METHOD HERE
# Change only this one line.
# --------------------------------------------------
CHUNKING_METHOD = "token"      # fixed | recursive | token

# --------------------------------------------------
# LOAD PDF
# --------------------------------------------------
documents = load_pdf("data/sample.pdf")

# --------------------------------------------------
# CHOOSE CHUNKING FUNCTION
# --------------------------------------------------
chunking_methods = {
    "fixed": fixed_chunking,
    "recursive": recursive_chunking,
    "token": token_chunking,
}

chunks = chunking_methods[CHUNKING_METHOD](documents)

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
print("\n" + "=" * 70)
print(f"CHUNKING METHOD : {CHUNKING_METHOD.upper()}")
print(f"TOTAL PDF PAGES : {len(documents)}")
print(f"TOTAL CHUNKS    : {len(chunks)}")
print("=" * 70)

# --------------------------------------------------
# PRINT EVERY CHUNK (FULL CONTENT)
# --------------------------------------------------
for i, chunk in enumerate(chunks, start=1):

    print("\n" + "#" * 70)
    print(f"CHUNK NUMBER : {i}")
    print(f"CHUNK ID     : {chunk.metadata['chunk_id']}")
    print(f"PDF PAGE     : {chunk.metadata['page'] + 1}")
    print(f"SOURCE FILE  : {chunk.metadata['source']}")
    print("-" * 70)

    # FULL CHUNK CONTENT
    print(chunk.page_content)

    print("#" * 70)