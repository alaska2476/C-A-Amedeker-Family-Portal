import streamlit as st

st.title("Administration")

st.warning(
    "Authorized Administrators Only"
)

tab1, tab2 = st.tabs([
    "Add Member",
    "Record Payment"
])

with tab1:

    st.subheader("Add Member")

    full_name = st.text_input(
        "Full Name"
    )

    phone = st.text_input(
        "Phone"
    )

    email = st.text_input(
        "Email"
    )

    if st.button("Add Member"):
        st.success(
            "Member Added"
        )

with tab2:

    st.subheader("Record Payment")

    member = st.text_input(
        "Member Name"
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    if st.button("Save Payment"):
        st.success(
            "Payment Recorded"
        )
