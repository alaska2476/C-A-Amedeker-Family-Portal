import streamlit as st
from database import get_members

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Member Accounts",
    layout="wide"
)

# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("Member Accounts")

# --------------------------------------------------
# LOAD MEMBERS
# --------------------------------------------------

members = get_members()

if members:

    member_options = {
        member[1]: member[0]
        for member in members
    }

    selected_member = st.selectbox(
        "Select Member",
        list(member_options.keys())
    )

    selected_member_id = member_options[selected_member]

    member_data = next(
        member
        for member in members
        if member[0] == selected_member_id
    )

    st.markdown("---")

    st.subheader("Member Information")

    st.write(member_data)

else:

    st.warning(
        "No members found."
    )
