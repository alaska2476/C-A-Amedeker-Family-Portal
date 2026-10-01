import streamlit as st

st.title("Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Contributions",
    f"GHC {total_contributions:,.2f}"
)

col2.metric(
    "Total Expenses",
    f"GHC {total_expenses:,.2f}"
)

col3.metric(
    "Cash Balance",
    f"GHC {cash_balance:,.2f}"
)

col4.metric(
    "Outstanding Levies",
    f"GHC {outstanding_levies:,.2f}"
)
