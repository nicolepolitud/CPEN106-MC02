import streamlit as st
from streamlit_community_navigation_bar import st_navbar
import pages as pg

# Set page config
st.set_page_config(
    page_title="Taal Lake Water Quality Dashboard",
    layout="wide",
    page_icon="lawatch.svg",
    initial_sidebar_state="collapsed"
)

# Define navigation pages
pages = ["ㅤHomeㅤ", "Dashboard", "Recommendations"]

# Custom styles for navbar
styles = {
    "nav": {
        "background-color": "#3b6203",
        "height": "6rem",
        "display": "flex",
        "align-items": "right",
        "justify-content": "space-between",
        "margin-bottom": "0",
    },
    "img": {
        "height": "4.5rem",
        "padding-right": "50rem",
    },
    "span": {
        "color": "white",
        "font-size": "1.2rem",
        "padding": "12px 20px",
        "font-weight": "bold",
    },
    "active": {
        "color": "#f8cc63",
        "font-weight": "bold",
    }
}

# Create navbar
page = st_navbar(
    pages,
    logo_path="lawatch.svg",
    styles=styles
)

# Define function routing
functions = {
    "ㅤHomeㅤ": pg.show_home,
    "Dashboard": pg.show_dashboard,
    "Recommendations": pg.show_rec
}

# Optional: Extra styling (e.g., underline or bar below navbar)
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
    }

    .nav-bottom-line {
        position: fixed;
        top: 6rem;
        left: 0;
        right: 0;
        height: 0.5rem;
        background-color: #1a4723;
        z-index: 9999;
    }
    </style>
    <div class="nav-bottom-line"></div>
""", unsafe_allow_html=True)

# Route to selected page
go_to = functions.get(page)
if go_to:
    go_to()
else:
    st.error("Page not found.")