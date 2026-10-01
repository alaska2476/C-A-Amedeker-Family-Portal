import streamlit as st
import pandas as pd

from database import initialize_database, get_members

initialize_database()
st.title("Members")

members = get_members()

if len(members) > 0:

    df = pd.DataFrame(
        members,
        columns=[
            "ID",
            "Full Name",
            "Phone",
            "Email",
            "Status"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No members have been added yet."
    )
