import streamlit as st
import sqlite3
conn = sqlite3.connect('db_memo.db')
cursor = conn.cursor()
load_id=st.text_input('공유코드를 입력하세요',max_chars=4)
if 'load_btn_click' not in st.session_state:
    st.session_state.load_btn_click = False

if 'load_data' not in st.session_state:
    st.session_state.load_data = None


save_btn=st.button('save')

row = cursor.fetchone()
if not st.session_state.load_btn_click:
    load_btn=st.button('load')
    if load_btn:
        cursor.execute(f"SELECT * FROM user WHERE memonum='{load_id}'")
        row = cursor.fetchone()
        if row:
            st.session_state.load_data = row[2]
            st.session_state.load_btn_click = True
        else:
            st.error('공유코드를 정확하게 기입하세요!')

if st.session_state.load_data:
    load_memo=st.text_area('load memo',st.session_state.load_data,height=1000)
else:
    load_memo=None

if save_btn:
    cursor.execute(f"SELECT * FROM user WHERE memonum='{load_id}'")
    row = cursor.fetchone()
    if row:
        if load_memo:
            sql=f"""UPDATE user SET memo ="{load_memo}" WHERE memonum = "{load_id}"
                    """
            cursor.execute(sql)
            conn.commit()
            st.success('저장 되었습니다')
        else:
            st.error('불러오기 버튼을 먼저 실행해 주세요')
    else:
        st.error('공유코드를 정확하게 기입하세요!')



