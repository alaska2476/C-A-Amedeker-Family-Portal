import streamlit as st

from database import initialize_database

initialize_database()

st.set_page_config(
    page_title="C.A. Amedeker Family Portal",
    layout="wide"
)

st.title("C.A. AMEDEKER FAMILY PORTAL")

st.info(
    "Use the menu on the left to navigate through the portal."
)
