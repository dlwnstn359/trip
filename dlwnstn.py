import streamlit as st
import folium
from streamlit_folium import folium_static

# 페이지 설정
st.set_page_config(page_title="수학여행 가이드", page_icon="🗺️", layout="wide")

# 사용자 정의 CSS
st.markdown(
    """
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .sub-title {
            font-size: 24px;
            color: #2980b9;
            margin-bottom: 10px;
        }
        .map-container {
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀
st.markdown("<div class='main-title'>📍 수학여행 가이드</div>", unsafe_allow_html=True)

# 지도 섹션
st.markdown("<div class='sub-title'>🌎 추천 여행 코스</div>", unsafe_allow_html=True)

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles='CartoDB positron')

# 예제 장소 데이터
locations = {
    "경복궁": [37.5796, 126.9770],
    "N서울타워": [37.5512, 126.9882],
    "롯데월드": [37.5112, 127.0980],
    "한강공원": [37.5262, 126.9326]
}

for name, coords in locations.items():
    folium.Marker(
        location=coords,
        popup=f"<b>{name}</b>",
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 표시
st.markdown("<div class='map-container'>", unsafe_allow_html=True)
folium_static(m)
st.markdown("</div>", unsafe_allow_html=True)


