# Jela Madalaga — Personal Portfolio Web App

A multipage personal portfolio web application built with **Streamlit** and **Python**.

---

## Pages

| Page | Description |
|------|-------------|
| **Home** | Introduction and overview |
| **About** | Personal profile, info, and capabilities |
| **Skills** | Skill bars showing proficiency levels |
| **Projects** | Project showcase and certificates |
| **Contact** | Contact form with validation |

---

## Features

- Multi-page navigation with sidebar
- Interactive contact form with input validation and dynamic feedback
- Project cards with images and tech tags
- Certificate gallery
- Skill progress bars
- Responsive dark-themed UI

---

## Project Structure

```
portfolio_app/
│
├── Home.py                  # Landing page
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
│
├── pages/
│   ├── 1_About.py           # About page
│   ├── 2_Skills.py          # Skills page
│   ├── 3_Projects.py        # Projects and certificates page
│   └── 4_Contact.py         # Contact form page
│
├── images/
│   ├── me.png               # Profile photo
│   ├── studymate.jpg        # Project image
│   ├── dormitory.jpg        # Project image
│   ├── GDFS5.jpg            # Project image
│   ├── 1stpython.png        # Certificate image
│   ├── Graphic_design.png   # Certificate image
│   ├── python.png           # Certificate image
│   ├── web_development.png  # Certificate image
│   └── Cyber_security.png   # Certificate image
│
└── .streamlit/
    └── config.toml          # Streamlit theme configuration
```

---

## Installation

1. Clone the repository:
```
git clone <your-repo-url>
cd portfolio_app
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the app:
```
streamlit run Home.py
```

---

## Requirements

- Python 3.8+
- Streamlit
- Pillow

---

## Developer

**Jela A. Madalaga**
BS Computer Science — 3rd Year
Mandaon, Masbate, PH
jlamdlg@gmail.com
