import streamlit as st

st.title("Administration")

st.warning("Authorized Administrators Only")

tab1, tab2, tab3, tab4 = st.tabs([
    "Add Member",
    "Add Levy",
    "Record Payment",
    "Audit Log"
])

# ----------------------------------
# ADD MEMBER
# ----------------------------------

with tab1:

    st.subheader("Add Member")

    full_name = st.text_input("Full Name")

    phone = st.text_input("Phone")

    email = st.text_input("Email")

    if st.button("Add Member"):
        st.success("Member Added")

# ----------------------------------
# ADD LEVY
# ----------------------------------

with tab2:

    st.subheader("Add Levy")

    member = st.text_input("Member Name")

    levy_amount = st.number_input(
        "Levy Amount",
        min_value=0.0
    )

    levy_description = st.text_input(
        "Levy Description"
    )

    if st.button("Create Levy"):
        st.success("Levy Added")

# ----------------------------------
# RECORD PAYMENT
# ----------------------------------

with tab3:

    st.subheader("Record Payment")

    member = st.text_input(
        "Member Name"
    )

    amount = st.number_input(
        "Payment Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Payment Description"
    )

    if st.button("Save Payment"):
        st.success("Payment Recorded")

# ----------------------------------
# AUDIT LOG
# ----------------------------------

with tab4:

    st.subheader("Audit Log")

    st.info(
        "Audit records will appear here."
    )
