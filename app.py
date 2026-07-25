import streamlit as st
from groq import Groq

client = Groq()  # reads GROQ_API_KEY from your environment automatically

SYSTEM_MESSAGE = {"role": "system", "content": "Keep every response to a maximum of 5 sentences."}

st.title("🎬 Movie Recommendation Buddy")

# initialize memory ONCE per session (survives reruns, resets on page refresh)
if "conversation" not in st.session_state:
    st.session_state.conversation = [SYSTEM_MESSAGE]

def chat(message):
    st.session_state.conversation.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.conversation
    )

    reply = response.choices[0].message.content
    st.session_state.conversation.append({"role": "assistant", "content": reply})
    return reply

def reset():
    st.session_state.conversation = [SYSTEM_MESSAGE]

# reset button
if st.button("🔄 New chat"):
    reset()
    st.rerun()

# display past turns (skip the system message)
for turn in st.session_state.conversation[1:]:
    with st.chat_message(turn["role"]):
        st.write(turn["content"])

# input box at the bottom
user_input = st.chat_input("Say something...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    reply = chat(user_input)

    with st.chat_message("assistant"):
        st.write(reply)

