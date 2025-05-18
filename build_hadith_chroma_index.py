import os
from dotenv import load_dotenv
load_dotenv()
# Загрузка переменных окружения из файла .env
assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY not found in environment."
# Проверка наличия ключа API OpenAI в окружении
# import langchain
# print(langchain.__version__)
import pandas as pd
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# === Configuration ===
PARQUET_PATH = "/Users/Tosha/Desktop/Hadith RAG/Project Hadith RAG/hadith_corpus_extended.parquet"
CHROMA_PATH = "chroma_hadith_index"
BATCH_SIZE = 1000  # Adjust based on your system's capabilities

# === Load the dataset ===
df = pd.read_parquet(PARQUET_PATH)

# === Initialize embeddings and Chroma vector store ===
embedding = OpenAIEmbeddings()
vectorstore = Chroma(embedding_function=embedding, persist_directory=CHROMA_PATH)

# === Process and add documents in batches ===
for i in range(0, len(df), BATCH_SIZE):
    batch_df = df.iloc[i:i + BATCH_SIZE]
    documents = []
    for _, row in batch_df.iterrows():
        uid = f"{row['collection_book']}-{row['book_id']}-{row['hadith_id_in_book']}"
        text = row["text_en"]
        metadata = row.to_dict()
        metadata["uid"] = uid
        doc = Document(page_content=text, metadata=metadata)
        documents.append(doc)
    vectorstore.add_documents(documents)

# === Persist the vector index ===
vectorstore.persist()
print(f"✅ Index successfully created at {CHROMA_PATH}")