import streamlit as st
from gtts import gTTS
from io import BytesIO
import random

# Updated content database with multiple lines per mood
sample_content = {
    "Motivation": {
        "Calm": [
            "Take a deep breath. Today, you take one small step closer to your dreams.",
            "Progress is still progress, no matter how slow.",
            "Peace is found in the present moment. Embrace it.",
            "Keep going. You're doing better than you think."
        ],
        "Energetic": [
            "Let’s go! The fire within you is stronger than the storm outside!",
            "You are built to succeed, to rise, to conquer!",
            "Attack the day with everything you've got!",
            "Your energy is contagious — spread it!"
        ],
        "Focus": [
            "Tune out the noise. Your goal deserves your full attention.",
            "Concentration is your superpower today.",
            "Silence the chaos. Focus on what matters.",
            "Let nothing distract you from your mission."
        ]
    },
    "Productivity": {
        "Calm": [
            "Start slow, build momentum. One task at a time gets the job done.",
            "Productivity flows when your mind is clear.",
            "Take a breath and prioritize what matters most.",
            "Work calmly, finish strong."
        ],
        "Energetic": [
            "Ready to crush your to-do list? Time to dominate the day!",
            "Let's power through the tasks with full force!",
            "Momentum is on your side — go for it!",
            "Every action you take is a step toward success."
        ],
        "Focus": [
            "Distractions can wait. This is your time to work deeply.",
            "Laser focus leads to massive progress.",
            "You’re in the zone — protect that energy.",
            "Deep work creates real results. Keep pushing."
        ]
    },
    "Self-Help": {
        "Calm": [
            "You are enough. Growth starts with self-kindness.",
            "Embrace the journey and be gentle with yourself.",
            "Healing begins when you allow yourself to feel.",
            "Be proud of how far you've come."
        ],
        "Energetic": [
            "You’re evolving! Embrace change and keep moving forward.",
            "You’ve got this. Nothing can stop your growth.",
            "Light up the world with your passion.",
            "Step into your power — now is your time."
        ],
        "Focus": [
            "Let’s reflect, realign, and rise. You’re in control.",
            "Center yourself — focus on your core values.",
            "Clarity is power. Stay locked in.",
            "Every focused thought brings you closer to your best self."
        ]
    },
    "News": {
        "Calm": [
            "Here’s a calm summary of today’s top stories, crafted just for you.",
            "Let’s take a relaxed look at the major global updates.",
            "No stress, just clarity. Here's what matters today.",
            "Take a moment to tune into the headlines in a peaceful tone."
        ],
        "Energetic": [
            "Let’s breeze through the headlines, full speed!",
            "Here’s your rapid-fire update on what’s happening.",
            "The world is buzzing — let’s catch up fast!",
            "Grab your attention — top news coming right up!"
        ],
        "Focus": [
            "No noise, just facts. Your personalized update is here.",
            "We’ll dive into the key stories with sharp focus.",
            "Your clear-cut headline report starts now.",
            "Skip the clutter — here’s what you need to know."
        ]
    }
}

# Streamlit page setup
st.set_page_config(page_title="VoiceCanvas AI", page_icon="🎧")
st.title("🎧 VoiceCanvas: Personalized Audio Experience")

genre = st.selectbox("🎼 Choose a Genre", list(sample_content.keys()))
mood = st.selectbox("🎭 Set the Mood", ["Calm", "Energetic", "Focus"])
duration = st.slider("🕒 Available Time (minutes)", 1, 15)

if st.button("🎙 Generate Your Audio"):
    st.info("Generating personalized audio... Please wait ⏳")

    try:
        # Approximate speech speed: ~130 words/minute
        target_word_count = duration * 130
        lines = sample_content[genre][mood]

        generated_text = ""
        used_lines = set()

        # Add lines randomly until word count target is reached
        while len(generated_text.split()) < target_word_count:
            line = random.choice(lines)
            if line not in used_lines or len(used_lines) == len(lines):
                generated_text += line + " "
                used_lines.add(line)

        # Add outro
        generated_text += f"This audio was generated for a {duration}-minute experience."

        # Convert to speech
        tts = gTTS(generated_text.strip(), lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        st.audio(audio_bytes, format="audio/mp3")
        st.success("✅ Done! Hit play and enjoy your VoiceCanvas session.")

    except Exception as e:
        st.error(f"❌ Error generating audio: {e}")
