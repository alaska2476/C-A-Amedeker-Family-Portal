import streamlit as st
import pandas as pd

from database import get_expenses

st.title("Expenses")

expenses = get_expenses()

if expenses:

    df = pd.DataFrame(
        expenses,
        columns=[
            "ID",
            "Date",
            "Type",
            "Description",
            "Amount"
        ]
    )

    df = df[
        [
            "Date",
            "Type",
            "Description",
            "Amount"
        ]
    ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No expenses have been recorded yet."
    )
