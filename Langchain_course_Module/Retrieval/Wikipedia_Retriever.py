from langchain_community.retrievers import WikipediaRetriever
import traceback

def main():
    try:
        # Create Wikipedia Retriever
        retriever = WikipediaRetriever(
            lang="en",
            top_k_results=2,
            doc_content_chars_max=500
        )

        # User Query
        query = "Artificial Intelligence"

        print(f"\nSearching Wikipedia for: {query}\n")

        # Retrieve documents
        docs = retriever.invoke(query)

        if not docs:
            print("No documents found.")
            return

        # Print documents
        for i, doc in enumerate(docs, start=1):
            print("=" * 60)
            print(f"Result {i}")
            print("=" * 60)

            print("Title :", doc.metadata.get("title", "N/A"))
            print("Source:", doc.metadata.get("source", "N/A"))

            print("\nContent:\n")
            print(doc.page_content)
            print("\n")

    except Exception as e:
        print("\nSomething went wrong!\n")
        print(type(e).__name__)
        print(e)

        print("\nFull Error:\n")
        traceback.print_exc()


if __name__ == "__main__":
    main()