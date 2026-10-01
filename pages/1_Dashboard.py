import streamlit as st

st.title("Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Members", 0)

with col2:
    st.metric("Levies", "$0.00")

with col3:
    st.metric("Payments", "$0.00")

with col4:
    st.metric("Outstanding", "$0.00")
