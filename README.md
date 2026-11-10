# CS Study Buddy AI

A local AI chatbot that quizzes you on Computer Science concepts using Llama 3 through Ollama.
Everything runs on your own computer, no API key needed.

## Setup

1. Install [Ollama](https://ollama.com) and download the model:
   ```bash
   ollama pull llama3
   ```
2. Create a virtual environment and install the dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run it:
   ```bash
   python3 main.py
   ```
