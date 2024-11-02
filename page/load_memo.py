import streamlit as st
import sqlite3
conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()
load_data='멋있는 내용을 불러와보세요'
load_id=st.text_input('공유코드를 입력하세요',max_chars=4)
load_btn=st.button('load')
save_btn=st.button('save')
row = cursor.fetchone()
if load_btn:
    cursor.execute(f"SELECT * FROM user WHERE memonum='{load_id}'")
    row = cursor.fetchone()
    if row:
        load_data = row[2]
        load_memo=st.text_area('Memo',load_data,height=1000)
    else:
        st.error('공유코드를 정확하게 기입하세요!')
if save_btn:
    if row:
        sql=f"""UPDATE user SET memo ="{load_memo}" WHERE memonum = "{load_id}"
                """
        cursor.execute(sql)
        conn.commit()
        st.success('저장 되었습니다')
    else:
        st.error('공유코드를 정확하게 기입하세요!')

        


