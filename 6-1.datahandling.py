import streamlit as st
import pandas as pd

st.text('1. 지하철 데이터 읽고 확인- data_subway_in_seoul.csv')   
# streamlit\data_subway_in_seoul.csv
# encoding='cp949'  읽어오고 확인하기 
df = 
st.dataframe()

st.text("2. 구분이 '하차'인 행만 새로운 데이터프레임으로 저장 & 확인") 
df_off = 
st.dataframe()

st.text("3. '날짜','연번','역번호','역명','구분','합계' 제외하고 저장 & 확인")
df_line = 
st.dataframe()

st.text("4. 아래 방법으로 데이터프레임 변환하여 저장 & 확인")
st.caption("melt 함수 사용 unpivot: identifier-'호선', unpivot column-'시간', value column-'인원수'")
df_line_melted = 
st.dataframe()

st.text("5. '호선','시간' 별 '인원수' 합,  as_index=False 저장 & 확인")
df_line_groupby = 
st.dataframe()


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-1.datahandling.py