import streamlit as st

from database import get_members

st.title("Members")

members = get_members()

if len(members) > 0:

    st.markdown("**ID      Name**")

    for member in members:
        st.text(f"{member[0]:<4} {member[11]}")

else:

    st.info("No members have been added yet.")
