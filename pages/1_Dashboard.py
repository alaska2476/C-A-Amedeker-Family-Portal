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

st.markdown("---")

# --------------------------------------------------
# RECENT ACTIVITY
# --------------------------------------------------

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

st.markdown("---")

# --------------------------------------------------
# CONTRIBUTIONS VS EXPENSES
# --------------------------------------------------

st.subheader(
    "Contributions vs Expenses Trend"
)

st.info(
    "Coming next: Green line = Contributions, Red line = Expenses."
)

st.markdown("---")

# --------------------------------------------------
# FUND STATUS
# --------------------------------------------------

if cash_balance >= 0:

    st.success(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )

else:

    st.error(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )
