import streamlit as st
import random as rd
import sqlite3
import time
conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()
memo=st.text_area('Memo',height=1000)



save=st.button('save',key='save_b')

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if save:
    while True:
        memo_id=rd.randint(1000,9999)
        cursor.execute(f"SELECT * FROM user WHERE memonum='{memo_id}'")
        row = cursor.fetchone()
        if not row:
            sql=f"""
            insert into user(memonum,memo)values('{memo_id}','{memo}')"""
            cursor.execute(sql)
            conn.commit()
            st.success(f'이 메모의 공유 코드는{memo_id}입니다')
            break
        
        else:
            print('다시시도중')