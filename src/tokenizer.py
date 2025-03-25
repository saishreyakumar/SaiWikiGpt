import json
import os
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from transformers import PreTrainedTokenizerFast

def train_tokenizer():
    with open("../data/wikipedia_text.json") as f:
        texts = json.load(f)

    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Whitespace()
    trainer = BpeTrainer(vocab_size=32000, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

    tokenizer.train_from_iterator(texts, trainer)


    project_dir = os.path.abspath(os.path.dirname(__file__))  
    tokenizer_dir = os.path.join(project_dir, "../models/tokenizer/")
    os.makedirs(tokenizer_dir, exist_ok=True)

    hf_tokenizer = PreTrainedTokenizerFast(
        tokenizer_object=tokenizer,
        unk_token="[UNK]",
        pad_token="[PAD]",
        bos_token="[CLS]",
        eos_token="[SEP]",
    )


    hf_tokenizer.save_pretrained(tokenizer_dir)


    config_path = os.path.join(tokenizer_dir, "tokenizer_config.json")
    with open(config_path, "r+") as f:
        config_data = json.load(f)
        config_data["model_type"] = "gpt2"  
        f.seek(0)
        json.dump(config_data, f, indent=4)

    print(f"Tokenizer saved successfully at {tokenizer_dir}")

if __name__ == "__main__":
    train_tokenizer()
