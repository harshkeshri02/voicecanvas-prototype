import streamlit as st
from gtts import gTTS
from io import BytesIO

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

st.set_page_config(page_title="VoiceCanvas AI", page_icon="🎧")
st.title("🎧 VoiceCanvas: Personalized Audio Experience")

genre = st.selectbox("🎼 Choose a Genre", list(sample_content.keys()))
mood = st.selectbox("🎭 Set the Mood", ["Calm", "Energetic", "Focus"])
duration = st.slider("🕒 Available Time (minutes)", 1, 15)

if st.button("🎙 Generate Your Audio"):
    st.info("Generating personalized audio... Please wait ⏳")

    # Approximate speech speed: ~130 words/minute
    target_word_count = duration * 130
    base_text = sample_content[genre][mood]
    full_text = base_text

    # Repeat/extend base_text until desired word count is met
    while len(full_text.split()) < target_word_count:
        full_text += " " + base_text

    # Add custom message
    full_text += f" This audio was generated for a {duration}-minute focused experience."

    try:
        # Convert to speech
        tts = gTTS(full_text, lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        st.audio(audio_bytes, format="audio/mp3")
        st.success("✅ Done! Hit play and enjoy your VoiceCanvas session.")

    except Exception as e:
        st.error(f"❌ Error generating audio: {e}")
