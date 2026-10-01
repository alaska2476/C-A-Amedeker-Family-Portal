import streamlit as st

st.title("Administration")

st.warning("Authorized Administrators Only")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Add Expense",
    "Record Payment",
    "Add Levy",
    "Add Member",
    "Audit Log"
])

# ----------------------------------
# ADD EXPENSE
# ----------------------------------

with tab1:

    st.subheader("Add Expense")

    expense_date = st.date_input(
        "Expense Date",
        key="expense_date"
    )

    expense_type = st.text_input(
        "Expense Type",
        key="expense_type"
    )

    expense_description = st.text_input(
        "Description",
        key="expense_description"
    )

    expense_amount = st.number_input(
        "Amount",
        min_value=0.0,
        key="expense_amount"
    )

    if st.button(
        "Save Expense",
        key="btn_save_expense"
    ):
        st.success("Expense Saved")

# ----------------------------------
# RECORD PAYMENT
# ----------------------------------

with tab2:

    st.subheader("Record Payment")

    member = st.text_input(
        "Member Name",
        key="payment_member"
    )

    payment_date = st.date_input(
        "Payment Date",
        key="payment_date"
    )

    amount = st.number_input(
        "Payment Amount",
        min_value=0.0,
        key="payment_amount"
    )

    description = st.text_input(
        "Payment Description",
        key="payment_description"
    )

    if st.button(
        "Save Payment",
        key="btn_save_payment"
    ):
        st.success("Payment Recorded")

# ----------------------------------
# ADD LEVY
# ----------------------------------

with tab3:

    st.subheader("Add Levy")

    member = st.text_input(
        "Member Name",
        key="levy_member"
    )

    levy_amount = st.number_input(
        "Levy Amount",
        min_value=0.0,
        key="levy_amount"
    )

    levy_description = st.text_input(
        "Levy Description",
        key="levy_description"
    )

    if st.button(
        "Create Levy",
        key="btn_create_levy"
    ):
        st.success("Levy Added")

# ----------------------------------
# ADD MEMBER
# ----------------------------------

with tab4:

    st.subheader("Add Member")

    full_name = st.text_input(
        "Full Name",
        key="member_full_name"
    )

    phone = st.text_input(
        "Phone",
        key="member_phone"
    )

    email = st.text_input(
        "Email",
        key="member_email"
    )

    if st.button(
        "Add Member",
        key="btn_add_member"
    ):
        st.success("Member Added")

# ----------------------------------
# AUDIT LOG
# ----------------------------------

with tab5:

    st.subheader("Audit Log")

    st.info(
        "Audit records will appear here."
    )

