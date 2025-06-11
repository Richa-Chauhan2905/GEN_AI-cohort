from dotenv import load_dotenv
from mem0 import Memory
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
import time
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URL = os.getenv("NEO4J_URL")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "text-embedding-3-small"},
    },
    "llm": {
        "provider": "openai",
        "config": {"api_key": OPENAI_API_KEY, "model": "gpt-4.1"},
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333},
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URL,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD,
        },
    },
}

mem_client = Memory.from_config(config)

# pdf_path = Path(__file__).parent / "little_red_riding_hood.pdf"
# loader = PyPDFLoader(file_path=pdf_path)
# docs = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200,
# )
# split_docs = text_splitter.split_documents(documents=docs)

# start_time = time.time()
# for i, doc in enumerate(split_docs):
#     print(f"Ingesting chunk {i+1}/{len(split_docs)}...")
#     mem_client.add(
#         messages=[{"role": "user", "content": doc.page_content}],
#         metadata={"source": f"chunk-{i}", **doc.metadata},
#         user_id="p123",
#     )

# print(f"Total ingestion time: {time.time() - start_time:.2f} seconds")
# print(f"Ingested {len(split_docs)} chunks into the memory.")

# mem = mem_client.get_all(
#     user_id="p123"
# )

mem = mem_client.search(
    query="What is the story of Little Red Riding Hood?", # this will provide the relations required acc to the question from the graph(realtions), then you can use openai for getting a perfect ans for the same
    user_id="p123"
)

print(mem)