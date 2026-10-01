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

st.subheader("Recent Activity")

left, right = st.columns(
    [1, 1],
    gap="large"
)

with left:

    st.markdown("### Recent Contributions")

    with st.container(border=True):

        if payments:

            st.dataframe(
                payments[-10:],
                use_container_width=True
            )

        else:

            st.info(
                "No contributions recorded."
            )

with right:

    st.markdown("### Recent Expenses")

    with st.container(border=True):

        if expenses:

            st.dataframe(
                expenses[-10:],
                use_container_width=True
            )

        else:

            st.info(
                "No expenses recorded."
            )

st.markdown("---")

# --------------------------------------------------
# CONTRIBUTIONS VS EXPENSES TREND
# --------------------------------------------------

st.subheader(
    "Contributions vs Expenses Trend"
)

with st.container(border=True):

    st.info(
        "Line chart will be displayed here. "
        "Green = Contributions, Red = Expenses."
    )

st.markdown("---")

# --------------------------------------------------
# FUND STATUS
# --------------------------------------------------

st.subheader("Fund Status")

if cash_balance >= 0:

    st.success(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )

else:

    st.error(
        f"Current Family Fund Balance: GHC {cash_balance:,.2f}"
    )
