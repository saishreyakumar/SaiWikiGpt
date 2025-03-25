import reflex as rx
from transformers import AutoTokenizer, GPT2LMHeadModel
import torch

# Load the model
model = GPT2LMHeadModel.from_pretrained("../models/wikipedia_gpt")
tokenizer = AutoTokenizer.from_pretrained("../models/tokenizer")

# App state
class State(rx.State):
    prompt: str = ""
    generated_text: str = ""
    max_tokens: int = 60
    history: list[tuple[str, str]] = []
    loading: bool = False

    def generate(self):
        self.loading = True
        self.generated_text = "Generating..."

        inputs = tokenizer(self.prompt, return_tensors="pt", padding=True)
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=self.max_tokens,
            do_sample=True,
            top_k=50,
            top_p=0.92,
            temperature=0.8,  # fixed value
            repetition_penalty=1.5,
            pad_token_id=tokenizer.eos_token_id,
        )

        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        final_output = decoded.split(".")[0] + "."

        self.generated_text = final_output
        self.history.append((self.prompt, final_output))
        self.loading = False

    def regenerate(self):
        self.generate()

# UI layout
def index():
    return rx.center(
        rx.container(
            rx.heading(" SaiWikiGPT Text Generator", size="4"),
            rx.text("Enter a prompt below and generate text."),
            rx.input(
                value=State.prompt,
                placeholder="Enter your prompt...",
                on_change=State.set_prompt,
                width="100%",
            ),
            rx.hstack(
                rx.button("Generate", on_click=State.generate, is_loading=State.loading),
                rx.button("Regenerate", on_click=State.regenerate, variant="outline"),
                spacing="4",
                margin_top="1em",
            ),
            rx.text("Max Tokens:"),
            rx.slider(
                min_=10,
                max_=100,
                step=10,
                value=[State.max_tokens],
                on_change=lambda val: State.set_max_tokens(val[0]),
            ),
            rx.text("Generated Output:", margin_top="2em", font_weight="bold"),
            rx.text(State.generated_text, margin_top="0.5em", white_space="pre-wrap"),
            rx.cond(State.history != [],
                rx.box(
                    rx.text("Prompt History:", font_weight="bold", margin_top="2em"),
                    rx.foreach(
                        State.history,
                        lambda item: rx.text(f"📝 {item[0]} → {item[1]}")
                    ),
                    margin_top="1em",
                    padding="1em",
                    border_radius="md",
                )
            ),
            padding="2em",
            max_width="700px",
        ),
        height="100vh"
    )

# Register app
app = rx.App()
app.add_page(index)
