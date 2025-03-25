from transformers import GPT2Config, GPT2LMHeadModel

def create_model():
    config = GPT2Config(
        vocab_size=32000,  
        n_embd=512,        
        n_layer=6,         
        n_head=8,          
    )
    model = GPT2LMHeadModel(config)
    return model

if __name__ == "__main__":
    model = create_model()
    print("Model initialized.")
