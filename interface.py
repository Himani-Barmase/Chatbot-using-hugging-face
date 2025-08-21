
from model_loader import load_chatbot_model
from chat_memory import ChatMemory

def run_chat():
    generator = load_chatbot_model("distilgpt2")
    memory = ChatMemory(window_size=5)

    print("Local CLI Chatbot (type /exit to quit)\n")

    while True:
        user_input = input("User: ")

        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        memory.add_turn("User", user_input)
        prompt = memory.get_context() + "\nBot:"
        response = generator(prompt, max_new_tokens=50, num_return_sequences=1)[0]["generated_text"]
        bot_reply = response.split("Bot:")[-1].strip().split("\n")[0]

        print(f"Bot: {bot_reply}")
        memory.add_turn("Bot", bot_reply)

if __name__ == "__main__":
    run_chat()
