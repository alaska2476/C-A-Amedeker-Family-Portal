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

    # --------------------------------------------------
    # MEMBER INFORMATION
    # --------------------------------------------------

    st.subheader("Member Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            f"**Name:** {member_data[1]}"
        )

    with col2:
        st.write(
            f"**Contribution Start Date:** {member_data[2]}"
        )

    st.markdown("---")

    # --------------------------------------------------
    # FINANCIAL SUMMARY
    # --------------------------------------------------

    st.subheader("Financial Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Expected",
            "GHC 0.00"
        )

    with col2:
        st.metric(
            "Total Paid",
            "GHC 0.00"
        )

    with col3:
        st.metric(
            "Total Outstanding",
            "GHC 0.00"
        )

    with col4:
        st.metric(
            "Last Contribution",
            "-"
        )

    st.markdown("---")

    # --------------------------------------------------
    # CONTRIBUTION HISTORY
    # --------------------------------------------------

    st.subheader("Contribution History")

    st.info(
        "Contribution history will appear here."
    )

    st.markdown("---")

    # --------------------------------------------------
    # MONTHLY BREAKDOWN
    # --------------------------------------------------

    st.subheader("Monthly Breakdown")

    st.info(
        "Expected, Paid and Outstanding amounts by month will appear here."
    )

    st.markdown("---")

    # --------------------------------------------------
    # TOTALS
    # --------------------------------------------------

    st.subheader("Totals")

    total1, total2, total3 = st.columns(3)

    with total1:
        st.metric(
            "Total Expected",
            "GHC 0.00"
        )

    with total2:
       tric(
            "Total Paid",
            "GHC 0.00"
        )

    with total3:
        st.metric(
            "Total Outstanding",
            "GHC 0.00"
        )

else:

    st.warning(
        "No members found."
    )
