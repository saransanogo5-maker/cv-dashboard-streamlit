import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# ======================================================
# CONFIG
# ======================================================
st.set_page_config(page_title="CV Dashboard - Saran Sanogo", layout="wide")

# ======================================================
# COULEURS GRAPHIQUES
# ======================================================
plot_bg = "rgba(0,0,0,0)"
paper_bg = "rgba(0,0,0,0)"

# ======================================================
# CSS GLOBAL + SIDEBAR
# ======================================================
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1f2933, #0f172a);
    padding: 24px 18px;
}

[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f9fafb;
    font-weight: 600;
    margin-bottom: 12px;
}

[data-testid="stSidebar"] hr {
    border: none;
    height: 1px;
    background-color: rgba(255,255,255,0.15);
    margin: 20px 0;
}

[data-testid="stSidebar"] img {
    border-radius: 14px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

[data-testid="stSidebar"] img:hover {
    transform: scale(1.03);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.35);
}

div[role="radiogroup"] > label {
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR - NAVIGATION
# ======================================================
st.sidebar.markdown("## 📌 Navigation")

section = st.sidebar.radio(
    "",
    ["Profil", "KPI Marketing", "Expériences", "Formations"]
)

st.sidebar.markdown("---")

# ======================================================
# RADAR COMPÉTENCES (SIDEBAR)
# ======================================================
skills_sidebar = pd.DataFrame({
    "Compétence": [
        "Gestion de projet",
        "Marketing Digital",
        "Analyse de données",
        "UX/UI",
        "CRM & Reporting"
    ],
    "Niveau": [5, 4, 4, 3, 4]
})

fig_sidebar_skills = px.line_polar(
    skills_sidebar,
    r="Niveau",
    theta="Compétence",
    line_close=True
)

fig_sidebar_skills.update_traces(fill="toself")

fig_sidebar_skills.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    margin=dict(l=20, r=20, t=20, b=20),
    height=260,
    font=dict(size=11),
    showlegend=False
)

st.sidebar.markdown("### 🕸️ Compétences clés")
st.sidebar.plotly_chart(fig_sidebar_skills, use_container_width=True)

st.sidebar.markdown("---")

# ======================================================
# QR CODE LINKEDIN
# ======================================================
st.sidebar.markdown("### 🔗 LinkedIn")
st.sidebar.image(
    "linkedin_qr.png",
    width=150,
    caption="Scanner pour voir mon profil"
)

# ======================================================
# PROFIL
# ======================================================
if section == "Profil":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("Saran Sanogo")
        st.subheader("Alternante Growth Manager | Marketing & Data")

        st.markdown("""
        📍 **Courbevoie, France**  
        📧 **saran.sanogo@gmail.com**
        """)

        st.write("""
        Passionnée par la gestion de projet digital et l’analyse de données,
        spécialisée en **Marketing & Data**.
        """)

    with col2:
        if os.path.exists("CV_Saran_Sanogo.pdf"):
            with open("CV_Saran_Sanogo.pdf", "rb") as file:
                st.download_button(
                    "📄 Télécharger mon CV",
                    file,
                    "CV_Saran_Sanogo.pdf",
                    "application/pdf"
                )
        else:
            st.warning("CV non trouvé")

# ======================================================
# KPI MARKETING
# ======================================================
elif section == "KPI Marketing":
    st.header("📊 KPI Marketing")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Engagement", "30%", "+10%")
    c2.metric("Conversion", "15%", "+5%")
    c3.metric("Visibilité", "40%", "+12%")
    c4.metric("Ventes Promo", "+20%", "+8%")

    df_kpi = pd.DataFrame({
        "Canal": ["SEO", "SEA", "Social Ads", "Email"],
        "Performance (%)": [50, 45, 35, 25]
    })

    fig = px.bar(df_kpi, x="Canal", y="Performance (%)", text="Performance (%)")
    fig.update_layout(plot_bgcolor=plot_bg, paper_bgcolor=paper_bg)

    st.plotly_chart(fig, use_container_width=True)

# ======================================================
# EXPERIENCES
# ======================================================
elif section == "Expériences":
    st.header("💼 Expériences professionnelles")

    experiences = [
        ("logos/paradise_game.png", "Cheffe de Projet Marketing & Événementiel",
         "Paradise Game – CDI",
         ["+30% taux d’engagement", "15+ événements", "+20% ventes promo"]),

        ("logos/manosa_connect.png", "Assistante Cheffe de Projet Digital",
         "Manosa Connect – Stage",
         ["+15% conversion", "+5% part de marché", "Backlog & user stories"]),

        ("logos/orange_ci.png", "Assistante Marketing Opérationnel",
         "Orange CI – Stage",
         ["+40% visibilité", "+35% trafic", "+50% CTR Ads"])
    ]

    for logo, title, company, points in experiences:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.subheader(title)
            st.write(f"**{company}**")
            for p in points:
                st.markdown(f"- {p}")
        st.divider()

# ======================================================
# FORMATIONS
# ======================================================
elif section == "Formations":
    st.header("🎓 Formations")

    formations = [
        ("logos/efrei.png", "BTS Réseau Informatique & Télécommunication", "EFREI Paris", "En cours"),
        ("logos/cestia.png", "Licence Marketing & Data", "Cestia Abidjan", "2018 – 2022")
    ]

    for logo, diploma, school, date in formations:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.subheader(diploma)
            st.write(f"**{school}**")
            st.caption(date)
        st.divider()
