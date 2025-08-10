import streamlit as st

st.set_page_config(page_title="India Then vs Now", layout="wide")

# Title
st.title("🇮🇳 India: Then vs Now")

# Sidebar navigation
menu = st.sidebar.radio("Navigate", ["Then vs Now", "Timeline", "Gallery", "About & CMS Vision"])

# Public working images
historical_image = "https://upload.wikimedia.org/wikipedia/commons/9/90/Chandni_Chowk%2C_Delhi%2C_ca_1900.jpg"
historical_image2 = "https://upload.wikimedia.org/wikipedia/commons/3/31/Varanasi_-_Benares%2C_India%2C_c._1905.jpg"
modern_image = "https://upload.wikimedia.org/wikipedia/commons/d/dc/Mumbai_Skyline_at_Night.jpg"
modern_image2 = "https://upload.wikimedia.org/wikipedia/commons/8/85/Bandra_Worli_Sea_Link_Mumbai.jpg"

# THEN vs NOW View
if menu == "Then vs Now":
    st.header("A Visual Contrast: Then vs Now")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Then (Early 1900s)")
        st.image(historical_image, caption="Chandni Chowk, Delhi - circa 1900", use_container_width=True)
        st.image(historical_image2, caption="Varanasi (Benares) - circa 1905", use_container_width=True)
    with col2:
        st.subheader("Now (Modern India)")
        st.image(modern_image, caption="Mumbai Skyline at Night", use_container_width=True)
        st.image(modern_image2, caption="Bandra-Worli Sea Link, Mumbai", use_container_width=True)

# Timeline View
elif menu == "Timeline":
    st.header("India Through the Years")
    st.markdown("""
    - **1900s** — Colonial India under British rule, traditional markets, bullock carts.
    - **1947** — Independence and partition; a new nation emerges.
    - **1950s-1980s** — Nation-building, dams, IITs, Green Revolution.
    - **1991** — Economic liberalization; global trade begins to reshape India.
    - **2000s** — IT boom, urban growth, globalization.
    - **2020s** — A global tech and space power.
    """)

# Gallery View
elif menu == "Gallery":
    st.header("Gallery")
    st.image(
        [historical_image, historical_image2, modern_image, modern_image2],
        caption=[
            "Chandni Chowk, Delhi - 1900s",
            "Varanasi - 1905",
            "Mumbai Skyline",
            "Bandra-Worli Sea Link"
        ],
        use_container_width=True
    )

# About & CMS Vision View
elif menu == "About & CMS Vision":
    st.header("About Group Captain Shubhanshu Shukla")
    st.markdown("""
    **Born:** 10 October 1985, Lucknow  
    **Profession:** Indian Air Force Test Pilot & ISRO Astronaut  
    
    Group Captain **Shubhanshu Shukla** is a decorated IAF test pilot and ISRO astronaut, 
    the first Indian in over 40 years to visit the International Space Station since Rakesh Sharma.  
    Selected in 2019 for India's human spaceflight ambitions, Shukla joined the elite Gaganyatri group, 
    undergoing rigorous training in Russia and India.  
    He flew as mission pilot on **Axiom Mission 4**, completing over 60 scientific experiments in space during 
    an 18-day orbit before safely returning.  
    His journey is a milestone for India’s space program, inspiring millions of students and young scientists.
    """)

    st.header("Vision of CMS (City Montessori School)")
    st.markdown("""
    *CMS instilled in me a spirit of curiosity, perseverance, and community — a foundation that guided me from 
    classroom ambition to the threshold of space.  
    I hope my journey inspires every young mind to dare beyond limits.*  

    CMS continues to foster global-minded learners ready to lead change, shaping students to become responsible 
    world citizens who contribute to peace and progress.
    """)

st.sidebar.info("Use the menu above to navigate through the sections.")
