import streamlit as st
from database import get_payments, get_expenses

# Get data
payments = get_payments()
expenses = get_expenses()

# Calculate totals
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

# Page Title
st.title("C.A. Amedeker Family Accounts")

st.caption(
    "Contributions • Expenses • Outstanding Levies"
)

st.subheader("Family Fund Summary")

# Summary Cards
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Contributions",
        f"GHC {total_contributions:,.2f}"
    )

with col2:
    st.metric(
        "Total Expenses",
        f"GHC {total_expenses:,.2f}"
    )

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Cash Balance",
        f"GHC {cash_balance:,.2f}"
    )

with col4:
    st.metric(
        "Outstanding Levies",
        f"GHC {outstanding_levies:,.2f}"
    )

st.markdown("---")

# Fund Status
if cash_balance >= 0:
    st.success(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )
else:
    st.error(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )

st.markdown("---")

# Recent Activity
left, right = st.columns(2)

with left:
    st.subheader("Recent Contributions")

    if payments:
        st.dataframe(
            payments[-5:],
            use_container_width=True
        )
    else:
        st.info("No contributions recorded.")

with right:
    st.subheader("Recent Expenses")

    if expenses:
        st.dataframe(
            expenses[-5:],
            use_container_width=True
        )
    else:
        st.info("No expenses recorded.")
