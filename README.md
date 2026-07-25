# Movie Recommendation Buddy ChatBot

A Streamlit-based movie recommendation chatbot that uses the Groq API for conversational memory.

## Features

- Simple Streamlit chat UI
- Conversation memory stored in session state
- System prompt enforces short responses (maximum 5 sentences)
- Uses `groq` Python client for `llama-3.3-70b-versatile`

## Requirements

- Python 3.10+
- `streamlit`
- `groq`
- `GROQ_API_KEY` set in your environment

## Install

```bash
python -m pip install streamlit groq
```

## Run

```bash
streamlit run app.py
```

## Usage

1. Open the local URL shown by Streamlit.
2. Enter a movie or recommendation prompt.
3. Chat with the assistant until you are done.
4. Click **New chat** to reset the conversation.

## Notes

- This app stores memory only during the current browser session.
- Make sure your `GROQ_API_KEY` is available in environment variables before running.
