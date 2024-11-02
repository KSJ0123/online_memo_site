import streamlit as st
pages = {
    "Memo" : [
        st.Page("./page/up_memo.py", title="memo"),
        st.Page("./page/load_memo.py",title="")
    ]
}
pg = st.navigation(pages)
pg.run()