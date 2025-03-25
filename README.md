# SaiWikiGpt: A Minimalist Wikipedia Language Model

## Problem Statement

> Train a minimal size language model on Wikipedia that can generate coherent responses. Justify your choices in architecture, tokenization and training strategy. Don't spend time building a web UI. Make it functional first.

## Model Architecture:

GPT2LMHeadModel with reduced layers for faster training.

## Training Data:

50,000 lines of cleaned Wikipedia text.

## Frameworks Used:

- Hugging Face Transformers & Datasets

- PyTorch backend

- Used Reflex to spend least time on UI

## Architecture Choices

### Model Architecture

- Small GPT-like architecture with 6 layers (vs the traditional GPT-2's 12 layers) basically a decoder like GPT
- Hidden size of 768 (same as BERT-base for good balance)
- 12 attention heads for parallel attention computation

**Reasoning for the Architecture used**: This architecture provides a good balance between model capacity and training efficiency.

### Tokenization

- Using GPT-2 tokenizer (inherits vocabulary and tokenization strategy)
- Maximum sequence length of 512 tokens
- BPE tokenization from GPT-2

**Reasoning for the Tokenization used**: GPT-2's tokenizer is well-tested and provides good coverage of English text while maintaining reasonable vocabulary size.

### Training Strategy

- Epochs = 5: Enough for convergence on small datasets without overfitting.
- Batch Size = 8: Works well with small VRAM setups.
- Learning Rate = 5e-4: Aggressive enough to speed up convergence for small models.

**Reasoning for the Training Strategy**: This is a proper trade-off between performance and speed, allowing training on CPU/low-tier GPU

## Project Structure

```
SAIWIKIGPT/

├── data/
│   └── wikipedia_text.json  # Wikipedia dataset
├── models/              # Model storage
│   └── tokenizer/      # Tokenizer files
├── SaiWikiGpt/
│   ├── __pycache__/
│   ├── __init__.py
│   └── SaiWikiGpt.py   # Reflex UI App
├── src/
│   ├── dataset.py     # Dataset
│   ├── generate.py    # Text model locally here
│   ├── model.py       # Model architecture
│   ├── tokenizer.py   # Tokenizer training (BPE)
│   └── train.py       # Model training logic
├── venv/              # Virtual environment
├── wandb/
├── README.md
├── requirements.txt
```

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

To train the model from scratch:

```bash
python src/train.py
```

### Model Configuration

The model configuration is defined in the training script with these key parameters:

```python
config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    n_embd=512,
    n_layer=6,
    n_head=8,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
)
```

- n_embd=512: Smaller embedding for faster training.
- n_layer=6: 6 transformer blocks, down from 12.
- n_head=8: 8 attention heads per block.

The training script will:

1. Download and cache the WikiText-2 dataset
2. Set up the GPT-2 tokenizer (or load existing model)
3. Initialize the model with specified configuration
4. Train the model
5. Save checkpoints and logs during training
6. Save the final model and tokenizer
