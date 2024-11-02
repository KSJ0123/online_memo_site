import streamlit as st
st.set_page_config(page_title="Memo_0123",page_icon="📃")
pages = {
    "Memo" : [
        st.Page("./page/up_memo.py", title="memo"),
        st.Page("./page/load_memo.py",title="")
    ]
}
pg = st.navigation(pages)
pg.run()