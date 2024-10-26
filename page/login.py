import streamlit as st
import sqlite3

    #데이터 베이스 연결
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
    #cursor.execute("SELECT * FROM user")

st.title("로그인")
id = st.text_input('아이디')
pw = st.text_input('비번',type='password')
btn = st.button('login')



if btn:
    cursor.execute(f"SELECT * FROM user WHERE username='{id}'")
    row = cursor.fetchone()
    if row:
        db_id = row[1]
        db_pw = row[2]
    else:
        db_id = ''
        db_pw = ''
        if db_pw == pw:
            st.sidebar.write(f"{id}님 환영합니다")
            st.switch_page("./page/memo.py")
        else:
            st.error("로그인 실패")
    ##st.switch_page("./page/d.py")