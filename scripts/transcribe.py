import whisper
import json
import os

model = whisper.load_model("large-v3")

audio_dir = "../data/audio"
output_dir = "../data/raw_text"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(audio_dir):
    if not file.endswith(".wav"):
        continue

    path = os.path.join(audio_dir, file)

    result = model.transcribe(
        path,
        language="ug",              # Force Uyghur
        task="transcribe",          # Do NOT translate
        initial_prompt="Bu audio Uyghur tilida sözlengen."
    )

    # Verify detected language
    detected_lang = result.get("language")
    print(f"{file} -> detected language: {detected_lang}")

    # Skip non-Uyghur outputs to avoid English hallucinations
    if detected_lang != "ug":
        print(f"Skipping non-Uyghur file: {file}")
        continue


    out_file = file.replace(".wav", ".json")
    with open(os.path.join(output_dir, out_file), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)