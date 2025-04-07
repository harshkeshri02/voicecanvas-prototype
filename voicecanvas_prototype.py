import streamlit as st
from gtts import gTTS
import os
import random

# Sample database of content per genre and mood
sample_content = {
    "Motivation": {
        "Calm": "Take a deep breath. Today, you take one small step closer to your dreams.",
        "Energetic": "Let’s go! The fire within you is stronger than the storm outside!",
        "Focus": "Tune out the noise. Your goal deserves your full attention."
    },
    "Productivity": {
        "Calm": "Start slow, build momentum. One task at a time gets the job done.",
        "Energetic": "Ready to crush your to-do list? Time to dominate the day!",
        "Focus": "Distractions can wait. This is your time to work deeply."
    },
    "Self-Help": {
        "Calm": "You are enough. Growth starts with self-kindness.",
        "Energetic": "You’re evolving! Embrace change and keep moving forward.",
        "Focus": "Let’s reflect, realign, and rise. You’re in control."
    },
    "News": {
        "Calm": "Here’s a calm summary of today’s top stories, crafted just for you.",
        "Energetic": "Let’s breeze through the headlines, full speed!",
        "Focus": "No noise, just facts. Your personalized update is here."
    }
}

st.title("VoiceCanvas: Personalized Audio Experience")

genre = st.selectbox("Choose a Genre", list(sample_content.keys()))
mood = st.selectbox("Set the Mood", ["Calm", "Energetic", "Focus"])
duration = st.slider("Available Time (minutes)", 1, 15)

if st.button("Generate Your Audio"):
    st.markdown("**Generating personalized audio...**")

    # Choose a sentence or generate dynamically
    text = sample_content[genre][mood]
    text += f" This audio is tailored for your {duration}-minute break."

    # Convert text to speech
    tts = gTTS(text)
    audio_file = "voicecanvas_output.mp3"
    tts.save(audio_file)

    st.audio(audio_file, format="audio/mp3")
    st.success("Done! Hit play and enjoy your VoiceCanvas.")

