import streamlit as st
import pandas as pd

from database import get_members

st.title("Members")

members = get_members()

if len(members) > 0:

    df = pd.DataFrame(
        members,
        columns=[
            "ID",
            "Name"
        ]
    )

    st.table(df)

else:

    st.info("No members have been added yet.")
