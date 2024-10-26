import streamlit as st
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
st.title("회원탈퇴")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
btn = st.button("탈퇴")

if btn:
    sql = f"""DELETE FROM user WHERE username="{id}"
    """
    cursor.execute(sql)
    conn.commit()