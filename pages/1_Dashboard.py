import streamlit as st
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

# Placeholder until Outstanding Levies is built
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
# MAIN DASHBOARD
# --------------------------------------------------

left, right = st.columns([1, 2])

# --------------------------------------------------
# LEFT SIDE
# --------------------------------------------------

with left:

    st.subheader("Family Fund Summary")

    st.metric(
        "Total Contributions",
        f"GHC {total_contributions:,.2f}"
    )

    st.metric(
        "Total Expenses",
        f"GHC {total_expenses:,.2f}"
    )

    st.metric(
        "Cash Balance",
        f"GHC {cash_balance:,.2f}"
    )

    st.metric(
        "Outstanding Levies",
        f"GHC {outstanding_levies:,.2f}"
    )

    st.markdown("---")

    if cash_balance >= 0:

        st.success(
            f"Available Family Fund Balance: GHC {cash_balance:,.2f}"
        )

    else:

        st.error(
            f"Family Fund Deficit: GHC {cash_balance:,.2f}"
        )

# --------------------------------------------------
# RIGHT SIDE
# --------------------------------------------------

with right:

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

    st.markdown("---")

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
