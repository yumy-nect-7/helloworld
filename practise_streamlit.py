import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.write('Hello world!')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20 , 30, 40]
})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('goodbye')

st.header('st.slider')
st.subheader('Slider')
age = st.slider('年齢?', 0, 130, 25)
st.write("私は", age, "歳")

st.subheader('Range slider')
values = st.slider(
    '値の範囲の指定',
    0.0, 100.0, (25.0, 75.0)
)
st.write("値: ", values)
