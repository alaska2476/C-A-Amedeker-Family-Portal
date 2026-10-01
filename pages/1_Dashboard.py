import streamlit as st
import pandas as pd
from database import get_payments, get_expenses

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="C.A. Amedeker Family Accounts",
    layout="wide"
)

# --------------------------------------------------
# GET DATA
# --------------------------------------------------

payments = get_payments()
expenses = get_expenses()

# --------------------------------------------------
# CALCULATE TOTALS
# --------------------------------------------------

total_contributions = (
    sum(payment[4] for payment in payments)
    if payments else 0
)

total_expenses = (
    sum(expense[4] for expense in expenses)
    if expenses else 0
)

cash_balance = total_contributions - total_expenses

# Placeholder until built
outstanding_levies = 0

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("C.A. Amedeker Family Accounts")

st.caption(
    "Contributions • Expenses • Outstanding Levies"
)

st.markdown("---")

# --------------------------------------------------
# TOP DASHBOARD ROW
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("Contributions")

    st.metric(
        "Total Contributions",
        f"GHC {total_contributions:,.2f}"
    )

    contribution_chart = pd.DataFrame(
        {
            "Amount": [total_contributions]
        }
    )

    st.bar_chart(
        contribution_chart,
        width="stretch"
    )

with right:

    st.subheader("Expenses")

    st.metric(
        "Total Expenses",
        f"GHC {total_expenses:,.2f}"
    )

    expense_chart = pd.DataFrame(
        {
            "Amount": [total_expenses]
        }
    )

    st.bar_chart(
        expense_chart,
        width="stretch"
    )

# --------------------------------------------------
# SECOND DASHBOARD ROW
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("Cash Position")

    st.metric(
        "Available Balance",
        f"GHC {cash_balance:,.2f}"
    )

    if cash_balance >= 0:

        st.success(
            f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
        )

    else:

        st.error(
            f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
        )

with right:

    st.subheader("Outstanding Levies")

    st.metric(
        "Outstanding Amount",
        f"GHC {outstanding_levies:,.2f}"
    )

    st.info(
        "Outstanding levy calculations will appear here."
    )

# --------------------------------------------------
# RECENT TRANSACTIONS
# --------------------------------------------------

st.markdown("---")

left, right = st.columns(2)

with left:

    st.subheader("Recent Contributions")

    if payments:

        st.dataframe(
            payments[-10:],
            width="stretch"
        )

    else:

        st.info(
            "No contributions recorded."
        )

with right:

    st.subheader("Recent Expenses")

    if expenses:

        st.dataframe(
            expenses[-10:],
            width="stretch"
        )

    else:

        st.info(
            "No expenses recorded."
        )

# --------------------------------------------------
# ACCOUNT SUMMARY
# --------------------------------------------------

st.markdown("---")

st.subheader("Account Summary")

summary_df = pd.DataFrame(
    {
        "Item": [
            "Total Contributions",
            "Total Expenses",
            "Cash Balance",
            "Outstanding Levies"
        ],
        "Amount (GHC)": [
            total_contributions,
            total_expenses,
            cash_balance,
            outstanding_levies
        ]
    }
)

st.dataframe(
    summary_df,
    width="stretch"
)
