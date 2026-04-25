import streamlit as st

st.set_page_config(layout="wide", page_title="Skills | Portfolio", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp {
    background: #000b1a;
    background-attachment: fixed;
}

header[data-testid="stHeader"] {
    background: #000b1a !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] {
    display: flex !important;
    visibility: visible !important;
    background: #1a1a1a !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

button[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
}

.skills-section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px 5%;
    transform: scale(0.95);
    transform-origin: top center;
}

.skills-header {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 10px;
    color: white;
}

.header-line {
    width: 60px;
    height: 2px;
    background-color: #ff4b2b;
    margin: 0 auto 40px auto;
}

.skill-container {
    margin-bottom: 20px;
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.skill-labels {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 15px;
    font-weight: 700;
    color: white;
}

.bar-track {
    background-color: #111;
    height: 6px;
    width: 100%;
    border-radius: 10px;
    overflow: hidden;
}

.bar-fill {
    background: linear-gradient(90deg, #ff4b2b, #ff8c00);
    height: 100%;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='skills-section'>
    <div class='skills-header'>My Skills</div>
    <div class='header-line'></div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class='skill-container'>
        <div class='skill-labels'><span>Python</span><span>40%</span></div>
        <div class='bar-track'><div class='bar-fill' style='width: 40%;'></div></div>
    </div>
    <div class='skill-container'>
        <div class='skill-labels'><span>UI & UX Design</span><span>65%</span></div>
        <div class='bar-track'><div class='bar-fill' style='width: 65%;'></div></div>
    </div>
    <div class='skill-container'>
        <div class='skill-labels'><span>Web Design</span><span>45%</span></div>
        <div class='bar-track'><div class='bar-fill' style='width: 45%;'></div></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='skill-container'>
        <div class='skill-labels'><span>HTML</span><span>50%</span></div>
        <div class='bar-track'><div class='bar-fill' style='width: 50%;'></div></div>
    </div>
    <div class='skill-container'>
        <div class='skill-labels'><span>CSS</span><span>70%</span></div>
        <div class='bar-track'><div class='bar-fill' style='width: 70%;'></div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
