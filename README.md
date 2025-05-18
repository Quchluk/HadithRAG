# 🕌 HadithRAG

**HadithRAG** is an open-source **Retrieval-Augmented Generation (RAG)** application designed for semantic question answering across large-scale hadith corpora. It integrates vector-based search (via **ChromaDB**) with modern language models to offer fast and intelligent access to classical Islamic texts.

> 🔬 **For researchers, students, and developers** at the intersection of Islamic studies and computational linguistics.

---

## 🚧 Status

**Under active development.**  
Core components are functional, but the interface, inference logic, and retrieval pipeline are being continuously refined.

---

## ✨ Features

- 📦 Preprocessed hadith corpus in `.parquet` format  
- 🧠 Vector index based on **ChromaDB** (excluded from repo; see below)
- ⚙️ CLI-based retrieval and index builder
- 🧱 Modular, scalable pipeline for large classical corpora

---

## 📚 Hadith Corpus

This project builds on the [Open Hadith Data](https://github.com/mhashim6/Open-Hadith-Data) collection curated by [Muhammad Hashim (mhashim6)](https://github.com/mhashim6). The corpus contains **over 50,000 authenticated hadiths** from nine canonical works, including the **Kutub al-Sittah (The Six Books)** — foundational to Sunni Islam.

These texts are central to Islamic theology (*ʿaqīdah*), law (*fiqh*), ethics, and intellectual tradition. Their inclusion here enables scalable, high-resolution analysis of a core civilizational archive using modern computational tools.

### 📘 Included Collections:

Each hadith is provided in **diacritized** and **undiacritized** Arabic, with metadata fields for book, chapter, isnād, and more.

- `📖` **Sahih al-Bukhari** (صحيح البخاري) — *Imam al-Bukhari*
- `📖` **Sahih Muslim** (صحيح مسلم) — *Muslim ibn al-Hajjaj*
- `📖` **Sunan Abu Dawud** (سُنن أبي داود) — *Abu Dawud al-Sijistani*
- `📖` **Jami‘ al-Tirmidhi** (جامع الترمذي) — *al-Tirmidhi*
- `📖` **Sunan al-Nasa’i** (السنن الصغرى) — *al-Nasa’i*
- `📖` **Sunan Ibn Majah** (سُنن ابن ماجه) — *Ibn Majah*
- `📖` **Musnad Ahmad ibn Hanbal** (مسند الإمام أحمد) — *Ahmad ibn Hanbal*
- `📖` **Muwatta Malik** (موطأ مالك) — *Malik ibn Anas*
- `📖` **Sunan al-Darimi** (سُنن الدارمي) — *al-Darimi*

Each entry includes full metadata such as book name, chapter, section, hadith number, and narrator chain (*isnād*), allowing for granular access and semantic filtering.

---

### 🗃️ Integration into This Project

To optimize the corpus for high-performance machine learning and semantic retrieval tasks, all hadiths were **converted from CSV into a unified `.parquet` format**:  
**`hadith_corpus_extended.parquet`**

This conversion ensures:

- 🔍 **Efficient vector indexing** (via ChromaDB or similar frameworks)
- 🚀 Fast queries over 50,000 entries
- 🧩 Ideal for integration into ML/NLP pipelines
- 🗜️ Compact storage with high I/O efficiency

This dataset serves as the **semantic backbone** of the HadithRAG application, enabling both accurate question answering and scalable research workflows in the digital humanities and Islamic NLP.

> 🧠 *HadithRAG represents one of the first practical RAG frameworks applied to a complete canonical hadith corpus, setting a foundation for future semantic reasoning systems in religious and historical textual domains.*

---

## 🧱 Rebuilding the Index

The `chroma_hadith_index/` folder is excluded due to GitHub's file size limits.

To rebuild the index locally:

```bash
python build_hadith_chroma_index.py
```

> 📦 Install dependencies first (see below).

---

## 💡 Usage

Coming soon:  
✅ Command-line queries  
✅ Retrieval examples  
✅ Full documentation

➡️ Entry point: `app.py`

---

## 🧭 Planned Features

- 🌐 Web UI via Streamlit
- 🌍 Multilingual output (Arabic / English / Russian)
- 🔎 Metadata filtering (book, topic, narrator)
- 🤗 HuggingFace Spaces integration
- ⚡ GPU-accelerated backend support

---

## ⚙️ Quick Start

```bash
git clone git@github.com:Quchluk/HadithRAG.git
cd HadithRAG
pip install -r requirements.txt  # (coming soon)
python build_hadith_chroma_index.py
```

---

## 👤 Author

**Anton Smirnov**  
🔗 GitHub: [Quchluk](https://github.com/Quchluk)

---

## 📄 License

This project is licensed under the **MIT License**.

---
