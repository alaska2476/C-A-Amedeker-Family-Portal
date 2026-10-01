import streamlit as st

st.set_page_config(
    page_title="C.A. Amedeker Family Portal",
    layout="wide"
)

st.title("C.A. AMEDEKER FAMILY PORTAL")

st.markdown("""
## Welcome

This portal provides access to:

- Family Accounts
- Levy Records
- Payment History
- Outstanding Balances
- Family Financial Records

### Family Members

✔ View all accounts

✔ View payment history

✔ Search family members

✔ View outstanding balances

### Administrators

✔ Add payments

✔ Add levies

✔ Update records

✔ Manage family accounts

---
""")

st.success("Family Portal Successfully Initialized")
