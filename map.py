# import streamlit as st
# import pandas as pd
# import numpy as np

# # 기본 형식
# def main():
#     # 화면에 관해 처리를 하고 싶다면 st를 사용해야한다.
#     st.title('시각화 팀 프로젝트')
#     # 대부분 main에서 작업을 한다.
#     st.subheader('제주도 여행지 시각화')
#     st.text('3조')
#     st.markdown('**아름다운 섬 제주**, 어디로 놀러가면 좋을까?')

# if __name__ == '__main__':
#     main()

# # number1

# st.text('첫번째 지도')
# # df = pd.DataFrame(
# #     np.random.randn(1000, 2) / [50, 50] + [33.4, 126.8],
# #     columns=['lat', 'lon'])

# # st.map(df)


# # number 2
# df1 = pd.read_csv('final_df_0425.csv')

# map_df = df1[['GPS X좌표','GPS Y좌표']]
# map_df.dropna(inplace=True)
# map_df.rename(columns = {'GPS X좌표' : 'lon', 'GPS Y좌표': 'lat'}, inplace = True)

# # print(df1.columns)

# st.map(map_df, color='성별')



import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# 여행지 방문 데이터 불러오기
# @st.cache 
data = pd.read_csv("final_df_0425.csv")
data.dropna(inplace=True)

# 지도 초기 위치 설정
map_center = [data['GPS Y좌표'].mean(),data['GPS X좌표'].mean()]

# 스트림릿 앱 제목 설정
st.title('여행지 방문 데이터 시각화')



# 성별 및 연령대 필터링 옵션 추가
gender = st.selectbox('성별 선택', ['남성', '여성'])
# age_range = st.slider('연령대 선택', min_value=0, max_value=100, value=(0, 100))
age = st.selectbox('연령대 선택', [20, 30, 40, 50, 60])
gender_dict = {"남성":"남", "여성":'여'}

# 필터링된 데이터셋 만들기
filtered_data = data
if gender != '전체':
    filtered_data = filtered_data[filtered_data['성별'] == gender_dict[gender]]
filtered_data = filtered_data[filtered_data['연령대'] == age]
# print(filtered_data)
# Folium을 사용하여 지도에 점 표시하기
map = folium.Map(location=map_center, zoom_start=11)
# folium.CircleMarker(location=(map_center[0],map_center[1]), radius=5, color='blue', fill=True).add_to(map)

for index, row in filtered_data.iterrows():
    folium.CircleMarker(location=(row['GPS Y좌표'], row['GPS X좌표']), radius=5, color='blue', fill=True).add_to(map)




# Folium 지도를 스트림릿에 추가
folium_static(map)
