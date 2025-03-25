import os
import json
import torch
from datasets import Dataset
from transformers import (
    GPT2LMHeadModel,
    GPT2Config,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)

# prep data
with open("../data/wikipedia_text.json") as f:
    texts = json.load(f)
    texts = texts[:50000] 

dataset = Dataset.from_dict({"text": texts})
dataset = dataset.train_test_split(test_size=0.05) 

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained("../models/tokenizer")

def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(type="torch", columns=["input_ids", "attention_mask"])

# Set up model
model_dir = "../models/wikipedia_gpt"
os.makedirs(model_dir, exist_ok=True)

if os.path.exists(os.path.join(model_dir, "pytorch_model.bin")):
    print("Loading existing model...")
    model = GPT2LMHeadModel.from_pretrained(model_dir)
else:
    config = GPT2Config(
        vocab_size=tokenizer.vocab_size,
        n_embd=512,
        n_layer=6,
        n_head=8,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    model = GPT2LMHeadModel(config)
    model.save_pretrained(model_dir)

# Training arguments
training_args = TrainingArguments(
    output_dir=model_dir,
    overwrite_output_dir=True,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=5,  
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=5e-4,
    weight_decay=0.01,
    logging_dir="../logs",
    logging_steps=50,
    save_total_limit=2,
    fp16=torch.cuda.is_available(),  
    gradient_checkpointing=True,
    report_to="none",  
)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    data_collator=data_collator,
)

# Train
if __name__ == "__main__":
    trainer.train()
    model.save_pretrained(model_dir)
    tokenizer.save_pretrained("../models/tokenizer")
