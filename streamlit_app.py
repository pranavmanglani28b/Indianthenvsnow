import streamlit as st

# App title
st.set_page_config(page_title="India Then vs Now - Defence & AI", layout="wide")
st.title("🇮🇳 India Then vs Now: Defence & AI Revolution")

# Introduction
st.markdown("""
India's journey from independence to the present day has been remarkable.
From modest defence capabilities and limited technology, we have grown into a
global leader in **artificial intelligence (AI)**, **modern warfare technology**, and **strategic defence**.
This interactive board takes you through the transformation.
""")

# --- THEN vs NOW Section ---
col1, col2 = st.columns(2)

with col1:
    st.header("🕰 Then: India's Defence & Tech (1947-2000)")
    st.image("then_image.jpg", caption="India's early defence era", use_column_width=True)
    st.markdown("""
    - **Limited defence budget** with focus on infantry and basic artillery.
    - Dependence on imports for advanced weaponry.
    - Manual communication and intelligence gathering.
    - Limited R&D facilities for defence.
    - Wars fought with minimal technological support.
    """)

with col2:
    st.header("⚡ Now: India's Defence & AI (2000-Present)")
    st.image("now_image.jpg", caption="Modern AI-driven defence", use_column_width=True)
    st.markdown("""
    - Indigenous weapons like **Tejas fighter jets**, **INS Vikrant**, and **Agni-V** missiles.
    - AI-powered **surveillance drones** and predictive defence systems.
    - Advanced **cybersecurity & cyber warfare capabilities**.
    - Space-based defence with **ISRO satellites**.
    - Global collaborations in AI and defence tech.
    """)

# --- AI in Defence ---
st.subheader("🤖 AI: The Game Changer in Defence")
st.markdown("""
Artificial Intelligence is revolutionising warfare:
- **Predictive threat analysis** using machine learning.
- AI-driven **autonomous drones** for reconnaissance.
- **Facial recognition** and biometric security for bases.
- Automated **logistics & supply chain** for the army.
- AI-assisted **missile guidance & target prediction**.

**India’s AI-driven defence** is now recognised globally for both speed and precision.
""")

# --- Shubhanshu Shukla & CMS Vision ---
st.header("🌟 Visionary Leadership: Shubhanshu Shukla & CMS")
st.image("cms_image.jpg", caption="City Montessori School", use_column_width=True)
st.markdown("""
**Shubhanshu Shukla**, an educator and visionary, emphasizes **holistic education**
that prepares students for a tech-driven future. At **City Montessori School (CMS)**,
the vision is:
- To **integrate AI awareness** from school level.
- To foster **critical thinking & innovation**.
- To inspire students to contribute to **national growth in technology & defence**.
""")

# --- Interactive Quiz ---
st.subheader("📝 Quick Quiz: Test Your Knowledge")
quiz_question = st.radio(
    "Which of these is NOT an AI application in defence?",
    ("Autonomous drones", "Predictive maintenance", "Paper-based telegrams", "Cyber threat detection")
)

if st.button("Check Answer"):
    if quiz_question == "Paper-based telegrams":
        st.success("✅ Correct! That's old tech, not AI.")
    else:
        st.error("❌ Nope! That's an AI application.")

# --- Closing ---
st.markdown("""
---
India’s **AI and defence journey** is a testament to vision, innovation, and resilience.
From humble beginnings to becoming a global power, the transformation is inspiring.
🇮🇳 **Jai Hind!**
""")
