# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if st.button('Say hello'): 
    st.write('Hello')
else:
    st.write('Goodbye')

st.header('2. Radio button')
genre = st.radio('좋아하는 영화장르를 선택하세요.', ('코미디','SF','액션'))
if genre == '코미디':
    st.write('코미디')
elif genre == 'SF':
    st.write('SF')
else:
    st.write('액션')




st.header('3. Checkbox')    # 😄
agree = st.checkbox('I agree')

if agree:
    st.write('★'*10)


st.header('4. Select box')
option = st.selectbox('어떻게 연락을 드릴까요??',('Email','Mobile phone', 'Office phone'))
st.write('네.',option,'알겠습니다.')

st.header('5. Multi select')
options = st.multiselect('좋아하는 색을 모두 선택해주세요.',['Green','Yellow','Red','Blue'],['Yellow','Red'])
st.write('선호 색상:', ', '.join(options))





st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title = st.text_input('최애 영화를 입력하세요.')
st.write('최애의영화 :',title)

st.subheader('**_number_input_**')
number = st.number_input('숫자를 입력하세요.',0)
st.write('입력한 숫자 :',number)

st.header('7. Date input')
ymd = st.date_input('생일이 언제인가요?')
st.write('생일: ',ymd)


st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되시나요??', 0, 100, 25)
st.write(age)

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values =  st.slider('범위 선택', 0, 25, (10,15))
st.write(values)


st.subheader('**_년 월 일 사이 구간_**')
slider_date = st.slider(
    '날짜 구간을 선택하세요',
    datetime(2022,1,1), datetime(2023,12,31),
    value= (datetime(2022,6,6), datetime(2022,11,10)),
    format='YY/MM/DD')

st.write('slider_date: ', slider_date)
st.write('slider_date[0]: ', slider_date[0])
st.write('slider_date[1]: ', slider_date[1])






# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py