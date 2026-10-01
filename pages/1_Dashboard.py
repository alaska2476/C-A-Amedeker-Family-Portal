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
# FAMILY FUND SUMMARY
# --------------------------------------------------

st.subheader("Family Fund Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Total Contributions**")
    st.markdown(
        f"## GHC {total_contributions:,.2f}"
    )

with col2:
    st.markdown("**Total Expenses**")
    st.markdown(
        f"## GHC {total_expenses:,.2f}"
    )

with col3:
    st.markdown("**Cash Balance**")
    st.markdown(
        f"## GHC {cash_balance:,.2f}"
    )

with col4:
    st.markdown("**Outstanding Levies**")
    st.markdown(
        f"## GHC {outstanding_levies:,.2f}"
    )

st.write("")
st.markdown("---")

# --------------------------------------------------
# RECENT ACTIVITY
# --------------------------------------------------

st.subheader("Recent Activity")

left, spacer, right = st.columns([5, 2, 5])

# --------------------------------------------------
# RECENT CONTRIBUTIONS
# --------------------------------------------------

with left:

    st.markdown("### Recent Contributions")

    if payments:

        contribution_df = pd.DataFrame(
            payments,
            columns=[
                "ID",
                "Date",
                "Member",
                "Contribution Type",
                "Amount"
            ]
        )

        contribution_df = contribution_df[
            [
                "Date",
                "Member",
                "Contribution Type",
                "Amount"
            ]
        ]

        st.dataframe(
            contribution_df.tail(10),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No contributions recorded."
        )

# --------------------------------------------------
# RECENT EXPENSES
# --------------------------------------------------

with right:

    st.markdown("### Recent Expenses")

    if expenses:

        expense_df = pd.DataFrame(
            expenses,
  
