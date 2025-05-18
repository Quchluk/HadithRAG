import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# === Paths ===
CHROMA_PATH = "chroma_hadith_index"

# === Initialize vector store and retriever ===
embedding = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# === Initialize LLM ===
llm = ChatOpenAI(model="gpt-3.5-turbo")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# === Streamlit UI ===
st.title("📖 HadithRAG")
query = st.text_input("Ask a question about Hadith:")

if query:
    result = qa_chain(query)
    st.markdown("## 🧠 LLM Response")
    st.write(result["result"])

    st.markdown("---")
    st.markdown("## 🔍 Source Hadiths")
    for i, doc in enumerate(result["source_documents"]):
        st.markdown(f"### {i+1}. Hadith")
        st.markdown(f"**Text:** {doc.page_content}")

        # Show metadata
        st.markdown("**Metadata:**")
        for k, v in doc.metadata.items():
            if v and v != "no data":
                st.markdown(f"- **{k}**: {v}")