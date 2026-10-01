import streamlit as st
import pandas as pd

st.title("Family Accounts")

data = pd.DataFrame({
    "Member": [
        "Anthony Toklo",
        "Deku Sefakor",
        "Amedeker Atsu",
        "Amedeker Mawufemor"
    ],
    "Levies": [1800, 1200, 3500, 2000],
    "Payments": [290, 670, 490, 1000]
})

data["Outstanding"] = (
    data["Levies"] - data["Payments"]
)

search = st.text_input(
    "Search Family Member"
)

if search:
    data = data[
        data["Member"]
        .str.contains(search, case=False)
    ]

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)
