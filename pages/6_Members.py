import streamlit as st
import pandas as pd

from database import (
    get_members,
    add_member
)

st.title("Members")

# ----------------------------------
# ADD MEMBER
# ----------------------------------

st.subheader("Add New Member")

member_name = st.text_input(
    "Member Name"
)

contribution_start_date = st.date_input(
    "Contribution Start Date"
)

if st.button("Add Member"):

    if member_name.strip():

        add_member(
            member_name,
            contribution_start_date
        )

        st.success(
            "Member added successfully."
        )

        st.rerun()

    else:

        st.error(
            "Please enter a member name."
        )

st.markdown("---")

# ----------------------------------
# MEMBER LIST
# ----------------------------------

members = get_members()

if len(members) > 0:

    df = pd.DataFrame(
        members,
        columns=[
            "ID",
            "Name",
            "Contribution Start Date"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No members have been added yet."
    )
