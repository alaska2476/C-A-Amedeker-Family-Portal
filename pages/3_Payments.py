import streamlit as st
import pandas as pd

from database import get_payments

st.title("Payments")

payments = get_payments()

if payments:

    df = pd.DataFrame(
        payments,
        columns=[
            "ID",
            "Date",
            "Member",
            "Description",
            "Amount"
        ]
    )

    df = df[
        [
            "Date",
            "Member",
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
        "No payments have been recorded yet."
    )
