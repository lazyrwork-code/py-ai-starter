from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# --- Konfigurasi ---
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-flash-latest"
SYSTEM_PROMPT = "Kamu adalah asisten AI yang helpful, jawab dengan ramah dan jelas dalam Bahasa Indonesia."

# --- Streamlit UI ---
st.set_page_config(page_title="ChatBot AI", page_icon="🤖", layout="centered")
st.title("🤖 ChatBot AI")
st.caption(f"Powered by Google Gemini · Model: {MODEL}")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []  # format: [{"role": "user/assistant", "content": "..."}]

# --- Helper: build prompt dengan history ---
def build_prompt(history: list[dict], user_input: str) -> str:
    lines = [SYSTEM_PROMPT, ""]
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"{role}: {msg['content']}")
    lines.append(f"User: {user_input}")
    lines.append("Assistant:")
    return "\n".join(lines)

# --- Helper: kirim ke Gemini ---
def send_message(history: list[dict], user_input: str) -> str:
    prompt = build_prompt(history, user_input)
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text.strip()

# --- Tampilkan riwayat chat ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Input user ---
if prompt := st.chat_input("Ketik pesan..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim ke Gemini & tampilkan response
    with st.chat_message("assistant"):
        with st.spinner("Sedang berpikir..."):
            reply = send_message(st.session_state.messages[:-1], prompt)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Tombol clear chat ---
if st.session_state.messages:
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()