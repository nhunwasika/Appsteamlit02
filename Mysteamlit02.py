import streamlit as st

import streamlit as st
st.image('./pic/dd.jpg')

col1,col2=st.columns(2)
with col1 :
    st.header('Wasika Jittisak')
with col2 :
    st.subheader('สาขาวิทยาการข้อมูล')
    st.text('คณะวิทยาศาสตร์และเทคโนโลยี')

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))
st.button('show bar chart')