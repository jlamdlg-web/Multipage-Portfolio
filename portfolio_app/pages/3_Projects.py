import streamlit as st
import base64
import os

st.set_page_config(page_title="Projects | Portfolio", page_icon="", layout="wide")

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
    padding-top: 1rem;
    padding-bottom: 3rem;
    max-width: 1200px;
    margin: 0 auto;
}

.main-header {
    text-align: center;
    color: #FF0000;
    font-size: 3.5rem;
    font-weight: 900;
    margin-top: 0;
    margin-bottom: 10px;
    letter-spacing: -0.02em;
}

.header-line {
    width: 80px;
    height: 3px;
    background: #FF0000;
    margin: 0 auto 30px auto;
    border-radius: 3px;
}

.project-card {
    background: #111111;
    border-radius: 15px;
    display: flex;
    align-items: center;
    padding: 20px;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s ease;
}

.project-card:hover {
    border-color: #FF0000;
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(255, 0, 0, 0.15);
}

.img-container {
    flex: 0 0 180px;
    height: 180px;
    background: #1a1a1a;
    border-radius: 12px;
    margin-right: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border: 1px solid rgba(255, 0, 0, 0.2);
}

.img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.text-container {
    flex: 1;
}

.project-title {
    color: #FF0000;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 5px;
}

.project-category {
    color: #FF6666;
    font-size: 0.8rem;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.project-desc {
    color: #cccccc;
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 12px;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tech-tag {
    background: rgba(255, 0, 0, 0.15);
    color: #FF8888;
    padding: 3px 10px;
    border-radius: 15px;
    font-size: 0.7rem;
    border: 1px solid rgba(255, 0, 0, 0.2);
}

.cert-section-label {
    text-align: center;
    color: #FF0000;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 40px 0 20px;
}

.cert-card {
    background: #111111;
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    overflow: hidden;
    transition: all 0.3s ease;
}

.cert-card:hover {
    border-color: #FF0000;
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(255, 0, 0, 0.15);
}

.cert-placeholder {
    width: 100%;
    height: 140px;
    background: #1a1a1a;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    font-size: 13px;
}

.cert-info {
    padding: 14px;
}

.cert-title {
    color: white;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 4px;
}

.cert-issuer {
    color: #FF6666;
    font-size: 11px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="main-header">PROJECTS</h1>
<div class="header-line"></div>
""", unsafe_allow_html=True)

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            ext = os.path.splitext(image_path)[1].lower()
            mime_type = "image/png" if ext == ".png" else "image/jpeg"
            return f"data:{mime_type};base64,{encoded}"
    except Exception:
        return None

projects = [
    {
        "title": "Studymate",
        "category": "WEB DEVELOPMENT",
        "desc": "A website that provides students a reminder for their upcoming projects and activities.",
        "tech": ["HTML", "CSS", "javaScript"],
        "image": "portfolio_app/images/studymate.jpg"
    },
    {
        "title": "Girl's Dormitory Management System",
        "category": "WEB DEVELOPMENT",
        "desc": "Project in AR102: A Girl Dormitory Management System that will streamline the process of inquering and monitor activities such as login and logout of the student and etc.",
        "tech": ["Microsoft Access", "MySQL"],
        "image": "portfolio_app/images/dormitory.jpg"
    },
    {
        "title": "GDF S5",
        "category": "EVENT SHOWCASE",
        "desc": "Event where we showcase our talent in Graphic Design and digital artistry.",
        "tech": ["Ibispaint app"],
        "image": "portfolio_app/images/GDFS5.jpg"
    }
]

for project in projects:
    tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in project["tech"]])
    img_data = get_image_base64(project["image"])
    img_src = img_data if img_data else f"https://via.placeholder.com/180x180/1a1a1a/FF0000?text={project['title'].replace(' ', '+')}"

    st.markdown(f"""
    <div class="project-card">
        <div class="img-container">
            <img src="{img_src}">
        </div>
        <div class="text-container">
            <div class="project-title">{project['title']}</div>
            <div class="project-category">{project['category']}</div>
            <div class="project-desc">{project['desc']}</div>
            <div class="project-tech">{tech_tags}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="cert-section-label">CERTIFICATES</div>', unsafe_allow_html=True)

certificates = [
    {"title": "Python Essential 1 Certificate", "issuer": "Cisco Networking Academy", "image": "portfolio_app/images/1stpython.png"},
    {"title": "Introduction to Graphic Design; Basics of UI/UX Certificate", "issuer": "Simplilearn", "image": "portfolio_app/images/Graphic_design.png"},
    {"title": "Python for Beginners Certificate", "issuer": "Simplilearn", "image": "portfolio_app/images/python.png"},
    {"title": "Web Development for Beginners Certificate", "issuer": "Simplilearn", "image": "portfolio_app/images/web_development.png"},
    {"title": "Introduction to Cyber Security Certificate", "issuer": "Simplilearn", "image": "portfolio_app/images/Cyber_security.png"},
]

cols = st.columns(5, gap="small")
for i, cert in enumerate(certificates):
    with cols[i]:
        img_data = get_image_base64(cert["image"]) if cert["image"] else None
        if img_data:
            img_html = f"<img src='{img_data}' style='width:100%; height:140px; object-fit:cover;'>"
        else:
            img_html = "<div class='cert-placeholder'>[ Certificate ]</div>"
        st.markdown(f"""
        <div class='cert-card'>
            {img_html}
            <div class='cert-info'>
                <div class='cert-title'>{cert['title']}</div>
                <div class='cert-issuer'>{cert['issuer']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
