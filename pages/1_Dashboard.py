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

# Placeholder until Outstanding Levies module is built
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
            columns=[
                "ID",
                "Date",
                "Expense Type",
                "Description",
                "Amount"
            ]
        )

        expense_df = expense_df[
            [
                "Date",
                "Expense Type",
                "Description",
                "Amount"
            ]
        ]

        st.dataframe(
            expense_df.tail(10),
            use_container_width=True,
            hide_index=True
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

if payments or expenses:

    chart_rows = []

    for payment in payments:

        chart_rows.append(
            {
                "Date": payment[1],
                "Contributions": payment[4],
                "Expenses": 0
            }
        )

    for expense in expenses:

        chart_rows.append(
            {
                "Date": expense[1],
                "Contributions": 0,
                "Expenses": expense[4]
            }
        )

    chart_df = pd.DataFrame(chart_rows)

    chart_df["Date"] = pd.to_datetime(
        chart_df["Date"]
    )

    chart_df = (
        chart_df
        .groupby("Date")
        .sum()
        .sort_index()
    )

    st.line_chart(
        chart_df,
        use_container_width=True
    )

else:

    st.info(
        "Add contributions and expenses to view the trend chart."
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
