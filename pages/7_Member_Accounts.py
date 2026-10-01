import streamlit as st
from database import get_members

st.set_page_config(
    page_title="Member Accounts",
    layout="wide"
)

st.title("Member Accounts")

members = get_members()

if members:

    member_options = {
        member[1\]: member[0]
        for member in members
    }

    selected_member = st.selectbox(
        "Select Member",
        list(member_options.keys())
    )

    st.success(
        f"Selected Member: {selected_member}"
    )

else:

    st.warning(
        "No members found."
    )
