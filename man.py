

import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd



# 비밀번호 설정
PASSWORD = "123"


# 상태 변수 사용
if "show_input" not in st.session_state:
    st.session_state.show_input = False

# Easter Egg 버튼 추가
if st.button("Easter Egg"):
    st.session_state.show_input = True

# 비밀번호 입력 필드 표시
if st.session_state.show_input:
    password_input = st.text_input("비밀번호를 입력하세요", type="password")
    
    # 비밀번호 검증
    if password_input:
        if password_input == PASSWORD:
            st.write("d임알")
        else:
            st.error("비밀번호가 틀렸습니다. 다시 시도하세요.")

