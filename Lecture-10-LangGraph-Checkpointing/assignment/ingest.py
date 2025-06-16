from pathlib import Path
from langchain.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from embedder import get_embedder

def ingest_py_to_qdrant():
    py_file_path = Path(__file__).parent / "stt.py"
    loader = TextLoader(file_path=str(py_file_path), encoding='utf-8')
    docs = loader.load()
    print("file loaded")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
    )
    split_docs = text_splitter.split_documents(documents=docs)
    print("splitting done")

    embedder = get_embedder()
    vector_store = QdrantVectorStore.from_documents(
        documents=[],
        url="http://localhost:6333",
        collection_name = "sts",
        embedding = embedder
    )
    print("embedding done")
    vector_store.add_documents(documents=split_docs)

    print("Ingested successfully")

if __name__ == "__main__":
    ingest_py_to_qdrant()