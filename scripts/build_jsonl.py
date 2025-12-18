import json

INPUT = "../data/final/clean_sentences.txt"
OUTPUT = "../data/final/uyghur_corpus.jsonl"

with open(INPUT, encoding="utf-8") as f, open(OUTPUT, "w", encoding="utf-8") as out:
    for line in f:
        record = {"text": line.strip()}
        out.write(json.dumps(record, ensure_ascii=False) + "\n")
# data/final/uyghur_corpus.jsonl will contain JSONL formatted Uyghur sentences.