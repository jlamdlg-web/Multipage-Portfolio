import streamlit as st

st.set_page_config(layout="wide", page_title="Jela Portfolio", initial_sidebar_state="expanded")

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

.block-container {
    padding: 4rem 5rem 2rem 5rem;
    max-width: 1200px;
}

.tag {
    display: inline-block;
    background: rgba(255, 69, 0, 0.08);
    border: 1px solid rgba(255, 69, 0, 0.3);
    color: #FF4500;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 7px 20px;
    border-radius: 50px;
    margin-bottom: 32px;
}

.intro {
    font-size: 20px;
    color: rgba(255, 255, 255, 0.5);
    font-weight: 300;
    margin-bottom: 10px;
}

.name {
    font-size: 78px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1;
    letter-spacing: -2px;
    margin-bottom: 6px;
}

.name-accent {
    color: #FF4500;
}

.role-text {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.4);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 30px;
}

.desc {
    font-size: 16px;
    color: rgba(255, 255, 255, 0.5);
    line-height: 1.9;
    max-width: 500px;
    margin-bottom: 44px;
    border-left: 3px solid #FF4500;
    padding-left: 20px;
}

.stat-num {
    font-size: 42px;
    font-weight: 900;
    color: #FF4500;
    line-height: 1;
}

.stat-lbl {
    font-size: 11px;
    color: rgba(255, 255, 255, 0.35);
    text-transform: uppercase;
    letter-spacing: 2px;
}

.img-wrap {
    padding: 3px;
    border-radius: 16px;
    background: linear-gradient(135deg, #FF4500, #ff8c00, transparent);
    margin-top: 40px;
}

.img-inner {
    border-radius: 14px;
    overflow: hidden;
    background: #0a1628;
}

.img-name-card {
    background: rgba(0, 11, 26, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 10px 18px;
    margin-top: 10px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("""
    <div style="padding-top: 30px;">
        <div class="tag">Open to Opportunities</div>
        <div class="intro">Hello, I'm</div>
        <div class="name">Jela<br><span class="name-accent">Madalaga</span></div>
        <div class="role-text">CS Student &amp; Aspiring Designer</div>
        <p class="desc">
            A 3rd-year Computer Science student with a passion for UI/UX and Graphic Design —
            turning ideas into clean, purposeful digital experiences.
        </p>
        <div style="display: flex; gap: 36px; margin-bottom: 48px;">
            <div><div class="stat-num">3+</div><div class="stat-lbl">Projects Done</div></div>
            <div><div class="stat-num">3rd</div><div class="stat-lbl">Year Level</div></div>
            <div><div class="stat-num">4+</div><div class="stat-lbl">Skills</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="img-wrap"><div class="img-inner">', unsafe_allow_html=True)
    try:
        st.image("../images/me.jpg", use_container_width=True)
    except:
        st.markdown("<div style='height:420px; background:#0a1628; display:flex; align-items:center; justify-content:center; color:#333;'>[ PHOTO ]</div>", unsafe_allow_html=True)
    st.markdown("""
        </div>
        <div class="img-name-card">
            <div style="font-size:15px; font-weight:700; color:white;">Jela Madalaga</div>
            <div style="font-size:11px; color:#FF4500; letter-spacing:1px; text-transform:uppercase; margin-top:2px;">CS Student · Designer</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
