import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="India: Then vs Now", layout="wide")

# -------------------------------
# Title and Introduction
# -------------------------------
st.title("🇮🇳 India: Then vs Now — The AI Revolution")
st.write("""
India has undergone a remarkable transformation in the past few decades.
From a largely agrarian economy to a technology powerhouse, the changes have been monumental.
One of the most significant forces shaping modern India is **Artificial Intelligence (AI)**.
Let's explore how AI has changed our nation and where it’s heading.
""")

# -------------------------------
# THEN vs NOW - Overview
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.header("India Then")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/e/ea/Indian_farmer_plowing_field.jpg",
        caption="Agriculture-driven economy in the past",
        use_container_width=True
    )
    st.write("""
    - Economy based on agriculture and manual labor.
    - Communication via letters and landline telephones.
    - Education heavily dependent on rote learning.
    - Industries were mostly manual with minimal automation.
    - Limited technological infrastructure.
    """)

with col2:
    st.header("India Now")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/5/5d/Bangalore_IT_park.jpg",
        caption="India's booming IT and AI industry",
        use_container_width=True
    )
    st.write("""
    - Digital-first economy with thriving tech startups.
    - AI-driven industries from healthcare to banking.
    - Smartphones and internet penetration even in rural areas.
    - Education powered by online learning platforms and AI tutors.
    - Smart agriculture, manufacturing, and logistics.
    """)

# -------------------------------
# AI in Modern India
# -------------------------------
st.subheader("📈 The Rise of Artificial Intelligence in India")
st.write("""
AI is no longer a futuristic concept — it's here and transforming lives daily.
From predicting crop yields for farmers to detecting diseases earlier than doctors,
AI is bridging gaps and opening new possibilities.
""")

ai_points = [
    "AI-based crop monitoring to help farmers improve yield.",
    "Automated medical diagnosis tools in rural clinics.",
    "Voice assistants supporting regional languages.",
    "AI-powered financial fraud detection.",
    "Traffic management systems in smart cities.",
    "Robotics in manufacturing and e-commerce."
]

for point in ai_points:
    st.markdown(f"✅ {point}")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/6/6f/Robotics_and_AI.jpg",
    caption="AI & Robotics in India",
    use_container_width=True
)

# -------------------------------
# Interactive Quiz
# -------------------------------
st.subheader("🧠 Quick AI Knowledge Quiz")
question = st.radio(
    "Which city is known as the 'Silicon Valley of India'?",
    ("Hyderabad", "Bengaluru", "Pune")
)
if question == "Bengaluru":
    st.success("🎉 Correct! Bengaluru is home to India's largest tech hub.")
else:
    st.error("❌ Not quite. It's Bengaluru.")

# -------------------------------
# Timeline
# -------------------------------
st.subheader("📜 India’s AI Timeline")
timeline_data = {
    "1990s": "Computers introduced widely, internet begins to spread.",
    "2000s": "IT boom, outsourcing industry grows rapidly.",
    "2010s": "Startups emerge focusing on AI and automation.",
    "2020s": "AI integrated into healthcare, education, finance, and governance."
}
for year, event in timeline_data.items():
    st.markdown(f"**{year}:** {event}")

# -------------------------------
# Conclusion
# -------------------------------
st.subheader("🚀 The Road Ahead")
st.write("""
AI will continue to shape India’s future.
With ethical use, proper regulation, and inclusive access, AI can bridge the gap between rural and urban India,
making our nation more efficient, equitable, and innovative.
""")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/d/d7/India_Futuristic_City_Concept.jpg",
    caption="Imagining India's AI-powered future",
    use_container_width=True
)
