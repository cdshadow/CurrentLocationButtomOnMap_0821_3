import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static

# 타이틀 설정
st.title("현위치 지도 표시")

# 위치 가져오기
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("대전")  # 기본 위치를 대전으로 설정

# Geolocation API를 통해 사용자 위치 가져오기
if st.button("내 위치 찾기"):
    user_input = st.text_input("위치 입력", "")
    if user_input:
        location = geolocator.geocode(user_input)  # 사용자가 입력한 위치로 설정

if location:
    st.write(f"위도: {location.latitude}, 경도: {location.longitude}")

    # 위치를 표시할 지도 생성
    m = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

    # 현위치에 마커 표시
    folium.Marker([location.latitude, location.longitude], tooltip="내 위치").add_to(m)

    # 지도를 스트림릿 앱에 표시
    folium_static(m)
