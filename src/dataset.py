import json
import os
from datasets import load_dataset

def load_wikipedia():
    dataset = load_dataset("wikipedia", "20220301.simple")
    texts = dataset["train"]["text"]

    cleaned_texts = [t.replace("\n", " ").strip() for t in texts if len(t) > 100]

    data_dir = os.path.join(os.getcwd(), "data")  
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, "wikipedia_text.json")

    with open(file_path, "w") as f:
        json.dump(cleaned_texts, f)

    print(f"Wikipedia dataset saved successfully at {file_path}")

if __name__ == "__main__":
    load_wikipedia()
