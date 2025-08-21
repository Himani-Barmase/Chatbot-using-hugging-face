
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def load_chatbot_model(model_name: str = "distilgpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )
    return generator
