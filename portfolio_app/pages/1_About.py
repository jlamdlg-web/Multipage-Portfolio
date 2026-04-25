import streamlit as st

st.set_page_config(layout="wide", page_title="About | Portfolio", initial_sidebar_state="expanded")

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
    padding: 0 !important;
    max-width: 100% !important;
}

.hero-banner {
    background: #000b1a;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding: 80px 8% 50px;
}

.banner-name {
    font-size: 72px;
    font-weight: 900;
    color: white;
    line-height: 0.95;
    letter-spacing: -3px;
}

.banner-name span {
    color: #FF4500;
}

.section-label {
    color: #FF4500;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.photo-card {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(255, 69, 0, 0.2);
    box-shadow: 0 40px 80px rgba(0, 0, 0, 0.6);
}

.info-row {
    display: flex;
    margin-bottom: 12px;
}

.info-label {
    color: white;
    font-weight: 700;
    width: 140px;
    font-size: 15px;
}

.info-value {
    color: #888;
    font-size: 15px;
}

.skill-pill {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: rgba(255, 255, 255, 0.7);
    padding: 8px 18px;
    border-radius: 50px;
    font-size: 13px;
    margin-right: 8px;
    margin-bottom: 8px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
    <div style="background: rgba(255,69,0,0.1); border: 1px solid rgba(255,69,0,0.25); color: #FF4500; font-size: 11px; font-weight: 700; padding: 6px 16px; border-radius: 50px; display: inline-block; margin-bottom: 20px;">
        PERSONAL PROFILE
    </div>
    <div class="banner-name">Jela<br><span>Madalaga</span></div>
    <div style="color: rgba(255,255,255,0.5); font-size: 14px; margin-top: 20px;">
        📍 Mandaon, Masbate &nbsp;•&nbsp; 🎓 BSCS — 3rd Year &nbsp;•&nbsp; ✉️ jlamdlg@gmail.com
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 1.3], gap="large")

with col1:
    st.markdown('<div style="padding: 40px 0 40px 8%;">', unsafe_allow_html=True)
    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
    try:
        st.image("portfolio_app/images/me.jpg", use_container_width=True)
    except:
        st.markdown("<div style='height:450px; background:#111; border-radius:24px; display:flex; align-items:center; justify-content:center; color:#333;'>[ PHOTO ]</div>", unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="padding: 40px 8% 40px 0;">', unsafe_allow_html=True)

    st.markdown('<div class="section-label">About Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color: rgba(255,255,255,0.6); line-height: 1.8; font-size: 15px; margin-bottom: 30px;">
        I am a 3rd-year Computer Science student who has fallen in love with the art of learning design.
        I find a unique satisfaction in structuring elements so they feel both logical and alive.
        I am actively building my design vocabulary and pushing the boundaries of what I can create.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Personal Info</div>', unsafe_allow_html=True)

    info_items = {
        "Name:": "Jela A. Madalaga",
        "Education:": "BS Computer Science (3rd Year)",
        "Address:": "Mandaon, Masbate, PH",
        "Zip Code:": "5411",
        "Email:": "jlamdg@gmail.com",
        "Phone:": "+63 9xx xxx xxxx"
    }

    for label, value in info_items.items():
        st.markdown(f"""
        <div class="info-row">
            <div class="info-label">{label}</div>
            <div class="info-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-label" style="margin-top: 30px;">Capabilities</div>', unsafe_allow_html=True)
    st.markdown("""
    <div>
        <span class="skill-pill">Graphic Design</span>
        <span class="skill-pill">UI/UX Design</span>
        <span class="skill-pill">Python</span>
        <span class="skill-pill">HTML & CSS</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
