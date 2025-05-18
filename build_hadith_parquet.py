import os
import json
import pandas as pd

# === PATH TO DATA ===
BASE_DIR = "/Users/Tosha/Desktop/Hadith RAG/Project Hadith RAG/data"

# === COLLECT ALL HADITH RECORDS ===
all_hadiths = []

# === WALK THROUGH ALL JSON FILES ===
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if not file.endswith(".json"):
            continue

        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, BASE_DIR)
        path_parts = relative_path.split(os.sep)

        collection_set = path_parts[0] if len(path_parts) > 0 else "no data"
        collection_book = path_parts[1] if len(path_parts) > 1 else "no data"
        chapter_file_name = path_parts[2] if len(path_parts) > 2 else file
        source_path = os.path.join(*path_parts)

        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                content = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Error reading file: {file_path}")
                continue

        meta_ar = content.get("metadata", {}).get("arabic", {})
        meta_en = content.get("metadata", {}).get("english", {})

        for h in content.get("hadiths", []):
            english = h.get("english", {})
            all_hadiths.append({
                # Core metadata
                "hadith_id": h.get("id", "no data"),
                "hadith_id_in_book": h.get("idInBook", "no data"),
                "book_id": h.get("bookId", "no data"),
                "chapter_id": h.get("chapterId", "no data"),

                # Text content
                "text_ar": h.get("arabic", "no data"),
                "text_en": english.get("text", "no data"),

                # English-side metadata
                "narrator_en": english.get("narrator", "no data"),
                "grade": english.get("grade", "no data"),
                "source": english.get("source", "no data"),
                "tags": english.get("tags", "no data"),
                "translator": english.get("translator", "no data"),
                "explanation": english.get("explanation", "no data"),
                "related_hadiths": english.get("relatedHadiths", "no data"),
                "location": english.get("location", "no data"),
                "subject": english.get("subject", "no data"),
                "collection": english.get("collection", "no data"),
                "volume": english.get("volume", "no data"),
                "page": english.get("page", "no data"),
                "section": english.get("section", "no data"),
                "commentary": english.get("commentary", "no data"),
                "keywords": english.get("keywords", "no data"),
                "narrator_chain": english.get("narratorChain", "no data"),
                "date": english.get("date", "no data"),
                "category": english.get("category", "no data"),

                # Arabic-side metadata (from file-level)
                "book_title_ar": meta_ar.get("title", "no data"),
                "book_title_en": meta_en.get("title", "no data"),
                "author_ar": meta_ar.get("author", "no data"),
                "author_en": meta_en.get("author", "no data"),
                "chapter_title_ar": meta_ar.get("introduction", "no data"),
                "chapter_title_en": meta_en.get("introduction", "no data"),

                # Folder-based metadata
                "collection_set": collection_set,
                "collection_book": collection_book,
                "chapter_file_name": chapter_file_name,
                "source_path": source_path
            })

# === CREATE DATAFRAME ===
df = pd.DataFrame(all_hadiths)

# === SAVE TO PARQUET FILE ===
output_file = "hadith_corpus_extended.parquet"
df.to_parquet(output_file, engine="pyarrow", index=False)

print(f"✅ Done: saved to {output_file}")
