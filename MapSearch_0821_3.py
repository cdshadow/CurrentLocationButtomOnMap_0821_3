import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import GoogleV3

# Google Geocoding API 키 설정
api_key = "AIzaSyCW-4kxARbJUxL3jmOz5dR5D-AabKhDJdc"  # 여기에 당신의 Google API 키를 입력하세요.

# Geopy 초기화 (GoogleV3 지오코더 사용)
geolocator = GoogleV3(api_key=api_key)

# 타이틀 설정
st.title("지도 검색")

# 위치 입력 필드
user_input = st.text_input("주소 검색", "대전")  # 기본 입력 값을 대전으로 설정

# 사용자가 버튼을 클릭하여 위치를 확인
if st.button("주소 또는 시설명 검색"):
    if user_input:
        location = geolocator.geocode(user_input)  # 사용자가 입력한 위치로 설정

        if location:
            # 위치 정보 표시
            st.write(f"위도: {location.latitude}, 경도: {location.longitude}")

            # 위치를 표시할 지도 생성
            m = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

            # 현위치에 마커 표시
            folium.Marker([location.latitude, location.longitude], tooltip="내 위치").add_to(m)

            # 지도를 Streamlit 앱에 표시
            folium_static(m)
        else:
            st.error("위치를 찾을 수 없습니다. 다시 시도해 주세요.")
