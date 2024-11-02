import streamlit as st
import random as rd
import sqlite3
conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()
memo=st.text_area('Memo',height=1000)
save=st.button('save')
conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()
if save:
    while True:
        memoid=None
        memo_id=rd.randint(1,4)
        cursor.execute(f"SELECT * FROM user WHERE memonum='{memo_id}'")
        row = cursor.fetchone()
        print(memo_id)
        print(memoid)
        if row:
            memoid=row[1]
            print(memoid)
        else:
            memoid=None
            print(memoid)
        if memoid != memo_id:
            sql=f"""
        insert into user(memonum,memo)values('{memo_id}','{memo}')"""
            cursor.execute(sql)
            conn.commit()
            st.success(f'이 메모의 공유 코드는{memo_id}입니다')
            break

def memo_check():
    print()