
# Local Command-Line Chatbot (LLM - Hugging Face)
##  Run
python interface.py

Local Command-Line Chatbot (LLM - Hugging Face) 

Task Overview
This project involves developing a fully functional local chatbot interface using a Hugging Face text generation model. The chatbot is designed to run in a command-line interface (CLI) and maintain conversational context through a sliding window mechanism.

Features

Local Model Execution: Loads and runs a small language model locally using Hugging Face's pipeline.


Conversational Memory: Maintains a short-term memory of previous exchanges using a sliding window buffer (e.g., the last 3-5 turns) to ensure coherent multi-turn conversations.


Robust CLI: Accepts continuous user input and terminates gracefully when the user types /exit.


Modular Code: The codebase is organized into three main Python scripts for clarity and maintainability:


model_loader.py: Handles model and tokenizer loading.


chat_memory.py: Contains the logic for the memory buffer.


interface.py: Manages the main CLI loop and integrates the other components.

Setup Instructions

Clone the repository or download the zipped folder.

Ensure you have Python installed on system.


Install the required libraries:


pip install transformers torch
How to Run
Navigate to the project directory and run the main interface script from terminal:


python interface.py
Sample Interaction
Once the script is running, the console will display the chatbot's prompt, and begin your conversation.

Local CLI Chatbot (type /exit to quit)

User: What is the capital of France? 
Bot: The capital of France is Paris.  
User: /exit 
Exiting chatbot. Goodbye! 
