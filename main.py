import streamlit as st
pages = {
    "Member" : [
        st.Page("./page/login.py", title="login"),
        st.Page("./page/sign_up.py", title="sign_up"),
        st.Page("./page/with.py", title="Withdrawal")
    ],
    "Memo" : [
        st.Page("./page/memo.py", title="memo")
    ]
}
pg = st.navigation(pages)
pg.run()