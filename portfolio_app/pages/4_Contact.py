import streamlit as st

st.set_page_config(layout="wide", page_title="Contact | Portfolio", initial_sidebar_state="expanded")

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
    max-width: 1500px;
    margin: auto;
}

.contact-hero p {
    color: #FF4500;
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 5px;
    margin-bottom: 20px;
}

.contact-hero h1 {
    font-size: 65px;
    font-weight: 900;
    color: white;
    line-height: 0.95;
    letter-spacing: -3px;
    margin: 0;
}

.info-sub-title {
    padding: 20px 0;
    font-size: 16px;
    color: #888;
    max-width: 380px;
    line-height: 1.6;
}

.contact-cards-row {
    display: flex;
    gap: 16px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.contact-card {
    background: rgba(255, 255, 255, 0.02);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.4s ease;
    flex: 1 1 0;
}

.contact-card:hover {
    background: rgba(255, 69, 0, 0.04);
    border: 1px solid rgba(255, 69, 0, 0.3);
    transform: translateY(-4px);
}

.card-marker {
    width: 30px;
    height: 3px;
    background: #FF4500;
    margin-bottom: 15px;
    border-radius: 10px;
}

.column-label {
    color: white;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 5px;
    display: block;
}

.column-detail {
    color: #888;
    font-size: 13px;
    text-decoration: none;
    display: block;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 10px !important;
    color: white !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #FF4500 !important;
    box-shadow: 0 0 0 2px rgba(255, 69, 0, 0.2) !important;
}

label {
    color: rgba(255, 255, 255, 0.6) !important;
    font-size: 13px !important;
}

div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #FF4500, #ff8c00);
    color: white;
    border: none;
    padding: 12px 36px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1px;
    width: 100%;
    margin-top: 8px;
    transition: opacity 0.3s;
}

div[data-testid="stButton"] > button:hover {
    opacity: 0.85;
}

.success-box {
    background: rgba(0, 200, 100, 0.08);
    border: 1px solid rgba(0, 200, 100, 0.3);
    border-radius: 14px;
    padding: 20px 24px;
    color: #00c864;
    font-size: 15px;
    font-weight: 600;
    margin-top: 16px;
    text-align: center;
}

.error-box {
    background: rgba(255, 69, 0, 0.08);
    border: 1px solid rgba(255, 69, 0, 0.3);
    border-radius: 14px;
    padding: 16px 20px;
    color: #FF4500;
    font-size: 13px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1.1, 1.3], gap="large")

with col_left:
    st.markdown("""
    <div class='contact-hero'>
        <p>Get in touch</p>
        <h1>Let's build<br>the future.</h1>
        <div class='info-sub-title'>
           I'm currently honing my design skills and ready to build
           something digital with you. Drop a message!
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='contact-cards-row'>
        <div class='contact-card'>
            <div class='card-marker'></div>
            <span class='column-label'>Email</span>
            <a href='mailto:jlamdlg@gmail.com' class='column-detail'>jlamdlg@gmail.com</a>
        </div>
        <div class='contact-card'>
            <div class='card-marker'></div>
            <span class='column-label'>Phone</span>
            <a href='#' class='column-detail'>+63 9xx xxx xxxx</a>
        </div>
        <div class='contact-card'>
            <div class='card-marker'></div>
            <span class='column-label'>LinkedIn</span>
            <a href='https://www.linkedin.com/in/jela-madalaga-00ba81382/' class='column-detail'>in/jela-madalaga</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("<div style='padding: 30px 0 0 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='color: #FF4500; font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 20px;'>Send a Message</div>", unsafe_allow_html=True)

    name = st.text_input("Your Name", placeholder="")
    email = st.text_input("Email Address", placeholder="")
    subject = st.selectbox("Subject", [
        "— Select a subject —",
        "Collaboration",
        "Project Inquiry",
        "Feedback",
        "Just Saying Hi 👋",
    ])
    message = st.text_area("Message", placeholder="Write your message here...", height=150)

    submitted = st.button("Send Message")

    if submitted:
        errors = []
        if not name.strip():
            errors.append("• Name is required.")
        if not email.strip() or "@" not in email:
            errors.append("• A valid email address is required.")
        if subject == "— Select a subject —":
            errors.append("• Please select a subject.")
        if not message.strip() or len(message.strip()) < 10:
            errors.append("• Message must be at least 10 characters.")

        if errors:
            st.markdown(f"<div class='error-box'>{'<br>'.join(errors)}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='success-box'>
                ✅ Message sent! Thanks, <strong>{name.split()[0]}</strong>!<br>
                <span style='font-size: 13px; font-weight: 400; color: rgba(0,200,100,0.8);'>
                    I'll get back to you at <strong>{email}</strong> soon.
                </span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
