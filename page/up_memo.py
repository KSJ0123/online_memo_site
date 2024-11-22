import streamlit as st
import random as rd
import sqlite3


conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()


memo = st.text_area('Memo', height=1000)


#변수 초기화
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
if 'memo_id' not in st.session_state:
    st.session_state.memo_id = None


if not st.session_state.button_clicked:
    save = st.button('save')
    if save:
        #메모코드 중복 처리
        while True:
            memo_id = rd.randint(1000,9999)
            cursor.execute(f"SELECT * FROM user WHERE memonum='{memo_id}'")
            row = cursor.fetchone()
            if not row:
                sql = f"INSERT INTO user (memonum, memo) VALUES ('{memo_id}', '{memo}')"
                cursor.execute(sql)
                conn.commit()
                #변수 저장
                st.session_state.button_clicked = True
                st.session_state.memo_id = memo_id
                break
            else:
                print('다시 시도 중')

if st.session_state.memo_id:
    st.success(f'이 메모의 공유 코드는 {st.session_state.memo_id}입니다.')
  