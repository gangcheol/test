import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import pandas as pd
import folium



st.set_page_config(layout='wide')

# 1. sidebar menu
with st.sidebar:   
    selected = option_menu("Do.nation", ["Home", 'NewsMap', 'Donation'], 
        icons=['house', 'bi bi-globe', 'bi bi-currency-exchange'], menu_icon="cast",
        styles={"nav-link-selected": {"background-color": "#9dd284"}})
        
    selected

# 2. Title
st.title('Do.Nation')

# 3. "Home" Page
if selected == 'Home':
    st.subheader('Welcome to our Homepage!')
    st.divider()
    
    # 소개
    st.header('About Us')
    intro = st.success('Do.Nation은 전 세계 뉴스 데이터를 기반으로 한 재난 및 전쟁 피해지역 기부 플랫폼입니다. 지도 위에 피해 지역의 심각도를 시각화 했으며 피해정도에 따라 기부하고자 하는 지역을 선택할 수 있습니다.')
    st.divider()
    
    # 뉴스맵 소개
    st.header('NewsMap')
    st.success('NewsMap이란 어쩌고 저쩌고')
    
    go_newsmap = st.button('뉴스맵 보러가기')

    
    
    # 기부방법 소개
    st.header('How to donate')
    st.success('방법 어쩌고 저쩌고')
    
    
    go_donate = st.button('기부하러 가기')

    st.divider()
    
# 4. NewsMap
if selected == 'NewsMap':
    st.subheader('NewsMap')
    path = r'C:\Users\user\aivle school\해커톤\folium\world_country_and_usa_states_latitude_and_longitude_values.csv'
    data = pd.read_csv(path)
    df = data.dropna(axis=0)
    place = df[ ['latitude', 'longitude'] ]
    place = place.values.tolist()
    
    map_country = folium.Map(location=[35, 127], zoom_start=4)

    def country(i,color):
        folium.Marker(
                location=point, 
                popup=df['country'][i],
                tooltip='Click!',
                icon=folium.Icon(color=color, icon='heart', icon_color='white' )
            ).add_to(map_country)

    i=0
    for point in place:
        country(i,'pink')
        i+=1
    st_folium(map_country, width=1400)
    
    
    