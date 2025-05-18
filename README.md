
⸻

HadithRAG

HadithRAG is an open-source Retrieval-Augmented Generation (RAG) application designed to enable semantic question answering over large-scale hadith corpora. By leveraging vector-based search with ChromaDB and modern language models, it provides researchers, students, and developers with efficient access to classical Islamic texts.

This project is intended to support digital research in Islamic studies, combining computational linguistics and scalable text retrieval to process thousands of narrations across canonical collections.

⚠️ The project is under active development. Core components are operational, but the interface and retrieval pipeline are being continuously improved.

⸻

Features
	•	Preprocessed hadith corpus in .parquet format
	•	Vector index based on ChromaDB (excluded from repository due to GitHub limitations)
	•	Local build and CLI-based retrieval interface
	•	Modular and scalable architecture suitable for large classical corpora

⸻

Status

🧪 This project is in early development. Contributions, issue reports, and suggestions are welcome.

⸻

## 📚 Hadith Corpus

This project is built upon one of the most comprehensive open-access datasets in the field of Islamic studies: the [Open Hadith Data](https://github.com/mhashim6/Open-Hadith-Data) collection curated by [Muhammad Hashim (mhashim6)](https://github.com/mhashim6). The dataset brings together over **50,000 authenticated hadiths** drawn from **nine classical collections**, including the **Kutub al-Sittah (The Six Canonical Books)**, which constitute the core of Sunni Islam’s hadith tradition.

These texts are foundational not only in Islamic theology (*ʿaqīdah*) and jurisprudence (*fiqh*), but also in historical linguistics, ethics, and Islamic intellectual history. For centuries, they have served as a basis for scholarly discourse, legal reasoning (*ijtihād*), and social practice across the Muslim world. Their canonical status makes them a uniquely valuable subject of computational exploration.

### 📘 Included Collections:

The dataset includes the following works, each provided in both **diacritized and undiacritized** Arabic, formatted for computational parsing:

- **Sahih al-Bukhari** (صحيح البخاري) — *Imam al-Bukhari (d. 870 CE)*
- **Sahih Muslim** (صحيح مسلم) — *Muslim ibn al-Hajjaj (d. 875 CE)*
- **Sunan Abu Dawud** (سُنن أبي داود) — *Abu Dawud al-Sijistani (d. 889 CE)*
- **Jami‘ al-Tirmidhi** (جامع الترمذي) — *al-Tirmidhi (d. 892 CE)*
- **Sunan al-Nasa’i** (السنن الصغرى) — *al-Nasa’i (d. 915 CE)*
- **Sunan Ibn Majah** (سُنن ابن ماجه) — *Ibn Majah (d. 887 CE)*
- **Musnad Ahmad ibn Hanbal** (مُسند الإمام أحمد بن حنبل) — *Ahmad ibn Hanbal (d. 855 CE)*
- **Muwatta Malik** (موطأ الإمام مالك) — *Malik ibn Anas (d. 795 CE)*
- **Sunan al-Darimi** (سُنن الدارمي) — *al-Darimi (d. 869 CE)*

Each entry includes full metadata such as book name, chapter, section, hadith number, and narrator chain (*isnād*), allowing for granular access and semantic filtering.

---

### 🗃️ Integration into This Project

To optimize the corpus for high-performance machine learning and semantic retrieval tasks, all hadiths were **converted from CSV into a unified `.parquet` format**:  
**`hadith_corpus_extended.parquet`**

This conversion ensures:

- **Efficient vector indexing** (via ChromaDB or similar frameworks)
- **High-speed queries and filtering**
- **Compatibility with large-scale RAG pipelines**
- **Compact storage for 50k+ entries** in a single, load-efficient binary format

This dataset serves as the **semantic backbone** of the HadithRAG application, enabling both accurate question answering and scalable research workflows in the digital humanities and Islamic NLP.

> 🧠 HadithRAG represents one of the first practical RAG frameworks applied to a complete canonical hadith corpus, setting a foundation for future semantic reasoning systems in religious and historical textual domains.

⸻

Rebuilding the Index

Due to GitHub’s file size restrictions, the chroma_hadith_index/ directory is not included in this repository.

To rebuild the index locally, run:

python build_hadith_chroma_index.py

Make sure to install the required packages beforehand (see below).

⸻

Usage

▶️ Usage examples will be provided here.
Please refer to app.py for an entry point to the current CLI interface.

⸻

Planned Features
	•	Web interface for interactive access
	•	Multilingual output (Arabic, English, Russian)
	•	Metadata-based filtering (by book, narrator, subject)
	•	Integration with Hugging Face Spaces and Streamlit
	•	Compatibility with GPU-accelerated backends

⸻

Quick Setup

Clone the repository and install dependencies:

git clone git@github.com:Quchluk/HadithRAG.git
cd HadithRAG
pip install -r requirements.txt  # ← to be added later

Then run the index builder:

python build_hadith_chroma_index.py


⸻

Author

Anton Smirnov
GitHub: Quchluk

⸻

License

📝 License will be added in a future release.

⸻

Если хочешь, я могу также добавить секцию с примерами запросов и выводов, когда ты их пришлёшь.
