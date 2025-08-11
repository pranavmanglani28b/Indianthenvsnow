import streamlit as st

st.set_page_config(page_title="India Then vs Now — AI Transformation", layout="wide")

# Title
st.title("🇮🇳 India Then vs Now — The AI Transformation")
st.markdown("### Exploring how AI has reshaped India's journey from the past to the present.")

# Tabs for Navigation
tabs = st.tabs(["Then vs Now", "AI in Different Sectors", "Vision of CMS", "About Shubhanshu Shukla"])

# ----------------- TAB 1: Then vs Now Overview -----------------
with tabs[0]:
    st.header("📜 India's Journey: Then vs Now")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Then (Pre-AI Era)")
        st.markdown("""
        - Depended on manual labor, traditional industries, and basic machinery.
        - Decisions in agriculture, governance, and healthcare relied entirely on human judgment.
        - Slow communication via letters, newspapers, and radio.
        - Education limited to physical classrooms and books.
        - Data was scattered, unused, and unstructured.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Indian_farmer_plowing_field.jpg", caption="Agriculture in early India", use_column_width=True)

    with col2:
        st.subheader("Now (AI-Powered Era)")
        st.markdown("""
        - AI-driven tools help in every sector from farming to finance.
        - Real-time decision-making through predictive analytics.
        - Instant communication and collaboration via the internet.
        - Personalized AI tutors and adaptive learning in classrooms.
        - AI processes massive data for better governance and innovation.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/AI_robot_india.jpg", caption="AI in modern India", use_column_width=True)

# ----------------- TAB 2: AI in Different Sectors -----------------
with tabs[1]:
    st.header("🤖 AI in Different Sectors — India’s Transformation")
    
    sectors = {
        "Agriculture": {
            "then_img": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Ploughing_with_oxen.jpg",
            "now_img": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Drone_in_agriculture.jpg",
            "then_text": "Farmers relied on experience and tradition to decide sowing and harvesting times.",
            "now_text": "AI predicts weather, detects crop diseases, and suggests the best planting times."
        },
        "Healthcare": {
            "then_img": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Old_hospital_india.jpg",
            "now_img": "https://upload.wikimedia.org/wikipedia/commons/b/b9/AI_healthcare.jpg",
            "then_text": "Diagnosis based on physical examination and limited technology.",
            "now_text": "AI reads scans, predicts health risks, and recommends treatments in seconds."
        },
        "Education": {
            "then_img": "https://upload.wikimedia.org/wikipedia/commons/6/67/Indian_rural_school.jpg",
            "now_img": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Online_learning.jpg",
            "then_text": "One-size-fits-all teaching with chalkboards and textbooks.",
            "now_text": "AI-powered platforms customize lessons for each student."
        }
    }

    for sector, data in sectors.items():
        st.subheader(sector)
        col1, col2 = st.columns(2)
        with col1:
            st.image(data["then_img"], caption=f"{sector} — Then", use_column_width=True)
            st.markdown(f"**Then:** {data['then_text']}")
        with col2:
            st.image(data["now_img"], caption=f"{sector} — Now", use_column_width=True)
            st.markdown(f"**Now:** {data['now_text']}")
        st.markdown("---")

# ----------------- TAB 3: Vision of CMS -----------------
with tabs[2]:
    st.header("🏫 The Vision of CMS (City Montessori School)")
    st.image("https://www.cmseducation.org/images/logo.png", caption="CMS Logo", width=200)
    st.markdown("""
    City Montessori School (CMS) envisions an **education system that nurtures world citizens**.
    Their focus is not only academic excellence but also **values, innovation, and global responsibility**.

    **Key Vision Points:**
    - Promote peace and unity through education.
    - Integrate technology and AI into learning.
    - Foster critical thinking and innovation among students.
    - Create socially responsible leaders of tomorrow.
    """)

# ----------------- TAB 4: About Shubhanshu Shukla -----------------
with tabs[3]:
    st.header("👨‍💼 About Shubhanshu Shukla")
    st.image("https://media.licdn.com/dms/image/D5603AQHTP1O1x0E8sw/profile-displayphoto-shrink_800_800/0/1704989116974?e=2147483647&v=beta&t=GxA5tZAC7nx6gIUVqO3Vsw0NhWB5prK5y-8mVa90ZoU",
             caption="Shubhanshu Shukla")
    st.markdown("""
    **Shubhanshu Shukla** is an educational leader and visionary at CMS, dedicated to integrating modern technology, 
    including AI, into the classroom.  
    He aims to prepare students for **a rapidly changing world** by focusing on:
    - Digital literacy
    - AI skills
    - Ethical leadership
    - Global perspective
    """)

st.success("✅ Interactive board loaded successfully! Explore the tabs to learn more about India's AI transformation.")
