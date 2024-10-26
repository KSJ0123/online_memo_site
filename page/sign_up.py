import streamlit as st
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

st.title('회원가입')
id = st.text_input('아이디')
pw = st.text_input('비번',type='password')
pw_2 = st.text_input('비번확인',type='password')
email = st.text_input('이메일')
btn2 = st.button('회원가입')
if btn2:
    if pw == pw_2:
        sql=f"""
insert into user(username,password,email,gender)values('{id}','{pw}','{email}')"""
        cursor.execute(sql)
        conn.commit()
        st.success('회원가입 성공!')
        st.switch_page("./page/memo.py")
    else:
        st.error('비밀번호를 다시 확인해 주세요')
conn.close()