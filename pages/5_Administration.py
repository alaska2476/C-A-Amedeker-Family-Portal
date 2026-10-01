import streamlit as st

from database import (
    initialize_database,
    add_member,
    get_members,
    update_member
)

initialize_database()

st.title("Administration")

st.warning("Authorized Administrators Only")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Members",
    "Expenses",
    "Payments",
    "Levies",
    "Audit Log"
])

# ----------------------------------
# MEMBERS
# ----------------------------------

with tab1:

    st.subheader("Add Member")

    full_name = st.text_input(
        "Member Name",
        key="member_full_name"
    )

    if st.button(
        "Add Member",
        key="btn_add_member"
    ):

        if full_name.strip():

            add_member(full_name)

            st.success(
                "Member Added Successfully"
            )

    st.markdown("---")

    st.subheader("Edit Member")

    members = get_members()

    if members:

        member_options = {
            f"{member[0]} - {member[1]}": member[0]
            for member in members
        }

        selected_member = st.selectbox(
            "Select Member",
            list(member_options.keys())
        )

        corrected_name = st.text_input(
            "Correct Name",
            key="corrected_member_name"
        )

        if st.button(
            "Update Member",
            key="btn_update_member"
        ):

            if corrected_name.strip():

                update_member(
                    member_options[selected_member],
                    corrected_name
                )

                st.success(
                    "Member Updated Successfully"
                )

    else:

        st.info(
            "No members available."
        )

# ----------------------------------
# EXPENSES
# ----------------------------------

with tab2:

    st.subheader("Expense Management")

    st.info(
        "Add, edit and delete expenses will be added next."
    )

# ----------------------------------
# PAYMENTS
# ----------------------------------

with tab3:

    st.subheader("Payment Management")

    st.info(
        "Add, edit and delete payments will be added next."
    )

# ----------------------------------
# LEVIES
# ----------------------------------

with tab4:

    st.subheader("Levy Management")

    st.info(
        "Add, edit and delete levies will be added next."
    )

# ----------------------------------
# AUDIT LOG
# ----------------------------------

with tab5:

    st.subheader("Audit Log")

    st.info(
        "Audit records will appear here."
    )
