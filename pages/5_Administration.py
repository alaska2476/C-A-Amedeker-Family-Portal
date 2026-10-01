import streamlit as st

from database import (
    initialize_database,
    add_member,
    get_members,
    update_member,
    add_expense,
    get_expenses,
    update_expense
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

    if st.button("Add Member", key="btn_add_member"):

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
            list(member_options.keys()),
            key="selected_member"
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

        st.info("No members available.")
# ----------------------------------
# EXPENSES
# ----------------------------------

with tab2:

    st.subheader("Add Expense")

    expense_date = st.date_input(
        "Transaction Date",
        key="expense_date"
    )

    expense_type = st.selectbox(
        "Expense Type",
        [
            "Electricity",
            "Water",
            "Housekeeping",
            "Funeral",
            "Transport",
            "Maintenance",
            "Meeting",
            "Administration",
            "Other"
        ],
        key="expense_type"
    )

    expense_description = st.selectbox(
        "Description",
        [
            "ECG Bill",
            "Water Bill",
            "Cleaning Services",
            "Funeral Contribution",
            "Transportation",
            "Repairs",
            "Meeting Refreshments",
            "Office Supplies",
            "Other"
        ],
        key="expense_description"
    )

    if expense_description == "Other":

        expense_description = st.text_input(
            "Enter Description",
            key="custom_expense_description"
        )

    expense_amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=0.01,
        key="expense_amount"
    )

    if st.button(
        "Save Expense",
        key="btn_save_expense"
    ):

        add_expense(
            expense_date,
            expense_type,
            expense_description,
            expense_amount
        )

        st.success(
            "Expense Saved Successfully"
        )

    st.markdown("---")

    st.subheader("Edit Expense")

    expenses = get_expenses()

    if expenses:

        expense_options = {
            f"{expense[0]} - {expense[2]}": expense[0]
            for expense in expenses
        }

        selected_expense = st.selectbox(
            "Select Expense",
            list(expense_options.keys()),
            key="selected_expense"
        )

        edit_date = st.date_input(
            "Transaction Date",
            key="edit_expense_date"
        )

        edit_type = st.selectbox(
            "Expense Type",
            [
                "Electricity",
                "Water",
                "Housekeeping",
                "Funeral",
                "Transport",
                "Maintenance",
                "Meeting",
                "Administration",
                "Other"
            ],
            key="edit_expense_type"
        )

        edit_description = st.selectbox(
            "Description",
            [
                "ECG Bill",
                "Water Bill",
                "Cleaning Services",
                "Funeral Contribution",
                "Transportation",
                "Repairs",
                "Meeting Refreshments",
                "Office Supplies",
                "Other"
            ],
            key="edit_expense_description"
        )

        if edit_description == "Other":

            edit_description = st.text_input(
                "Enter Description",
                key="edit_custom_expense_description"
            )

        edit_amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=0.01,
            key="edit_expense_amount"
        )

        if st.button(
            "Update Expense",
            key="btn_update_expense"
        ):

            update_expense(
                expense_options[selected_expense],
                edit_date,
                edit_type,
                edit_description,
                edit_amount
            )

            st.success(
                "Expense Updated Successfully"
            )

    else:

        st.info(
            "No expenses available."
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

