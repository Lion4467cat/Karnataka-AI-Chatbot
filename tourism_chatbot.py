import streamlit as st
import requests
from datetime import datetime

# === CONFIG ===
GROQ_API_KEY = "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"  # Replace with your actual key
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}
MODEL = "llama-3.1-8b-instant"

# === STREAMLIT SETUP ===
st.set_page_config(
    page_title="Karnataka Tourism Chatbot",
    page_icon="🏞️",
    layout="centered",
    # theme is now driven by .streamlit/config.toml
)

st.title("🏞️ Karnataka Tourism Chatbot")
st.markdown(
    "Welcome to your dark-mode Karnataka travel assistant! Ask me anything about destinations, itineraries, and insider tips."
)

# === SESSION STATE INITIALIZATION ===
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": "You are a helpful assistant that recommends places in Karnataka.",
        }
    ]


# === FUNCTION TO CALL GROQ API ===
def query_groq(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
    }
    resp = requests.post(API_URL, headers=HEADERS, json=payload)
    if resp.status_code == 200:
        return resp.json()["choices"][0]["message"]["content"]
    else:
        st.error(f"GROQ API Error {resp.status_code}: {resp.text}")
        return None


# === CHAT INTERFACE ===
user_input = st.chat_input("Type your question about Karnataka…")

if user_input:
    # record & send
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Thinking…"):
        reply = query_groq(st.session_state.chat_history)
    if reply:
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# === RENDER MESSAGES ===
for msg in st.session_state.chat_history[1:]:
    is_user = msg["role"] == "user"
    avatar = "🧑‍💻" if is_user else "🤖"
    with st.chat_message("user" if is_user else "assistant", avatar=avatar):
        st.markdown(msg["content"])

# === TIMESTAMP ===
st.sidebar.markdown(f"🔄 Last update: {datetime.now():%Y-%m-%d %H:%M:%S}")
