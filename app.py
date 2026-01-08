import streamlit as st
from gtts import gTTS
import uuid
import os

# -----------------------------
# Supported languages
# -----------------------------
LANGUAGES = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Bengali": "bn",
    "Marathi": "mr",
}

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Arkay Multilingual TTS", page_icon="🔊", layout="centered")

st.title("🔊 Arkay Multilingual TTS")
st.write("Simple, fast, and reliable Indian & global language Text-to-Speech using Google TTS.")

text = st.text_area("Enter Text", height=150)
language_name = st.selectbox("Select Language", list(LANGUAGES.keys()))

if st.button("Generate Speech"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        lang_code = LANGUAGES[language_name]

        filename = f"tts_{uuid.uuid4().hex}.mp3"

        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(filename)

        st.success("Speech generated successfully!")

        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        # Optional: cleanup old files later (not needed for Streamlit Cloud MVP)
