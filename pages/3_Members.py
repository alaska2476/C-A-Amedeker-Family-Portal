import streamlit as st
import pandas as pd

st.title("Family Members")

members = pd.DataFrame({
    "Name": [
        "Anthony Toklo",
        "Deku Sefakor",
        "Amedeker Atsu"
    ],
    "Phone": [
        "",
        "",
        ""
    ]
})

st.dataframe(
    members,
    use_container_width=True,
    hide_index=True
)
