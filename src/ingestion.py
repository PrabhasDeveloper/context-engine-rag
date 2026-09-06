from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Load a PDF file and return LangChain Document objects.
    """

    # Create the PDF loader
    loader = PyPDFLoader(file_path)

    # Read every page from the PDF
    documents = loader.load()

    return documents


def display_documents(documents):
    """
    Print metadata and preview text from each page.
    """

    print("=" * 60)
    print(f"Total Pages Loaded : {len(documents)}")
    print("=" * 60)

    for index, doc in enumerate(documents):

        print(f"\nPage Number : {doc.metadata['page'] + 1}")
        print(f"Source File : {doc.metadata['source']}")

        print("\nExtracted Text Preview:")
        print("-" * 40)

        # Show only first 300 characters
        print(doc.page_content[:300])

        print("\n" + "=" * 60)
