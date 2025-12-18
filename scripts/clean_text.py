import json
import os
import regex as re

RAW_DIR = "../data/raw_text"
CLEAN_TXT = "../data/final/clean_sentences.txt"
os.makedirs("../data/final", exist_ok=True)

def clean(sentence):
    sentence = re.sub(r"\[.*?\]|\(.*?\)", "", sentence)
    sentence = re.sub(r"http\S+", "", sentence)
    sentence = re.sub(r"\d+:\d+", "", sentence)
    sentence = sentence.strip()
    return sentence

with open(CLEAN_TXT, "w", encoding="utf-8") as out:
    for file in os.listdir(RAW_DIR):
        with open(os.path.join(RAW_DIR, file), encoding="utf-8") as f:
            data = json.load(f)

        for seg in data["segments"]:
            text = clean(seg["text"])
            if len(text) < 10:
                continue
            if text.count("的") > 1:  # Chinese noise filter
                continue
            out.write(text + "\n")