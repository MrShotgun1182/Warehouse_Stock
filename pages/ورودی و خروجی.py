import streamlit as st
from Engin import *

st.set_page_config(page_title="ورودی و خروجی انبار")

st.write("# :جدول ورودی و خروجی انبار")

st.dataframe(make_i_o_DF(), use_container_width=True, selection_mode="multi-row")

st.write("# :افزودن داده جدید")

with st.form('myform'):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        i_oType = st.radio('ورودی / خروجی', options=['ورودی', 'خروجی'])

    with col2:
        ProductName = st.selectbox("نام کالا", list(make_dic("Products").values()), placeholder='*')

    with col3:
        Number = st.number_input(label="تعداد", placeholder='*', step=1)
        submit = st.form_submit_button("درج کردن")
        
    with col4: 
        Pric = st.number_input(label="قیمت هر واحد", placeholder='*', step=1)     
        
    with col5:
        date = st.text_input(label="تاریخ", value=date(), placeholder=date())
    
    

if submit:
    input_list = [i_oType, ProductName, Pric, Number, date]
    result = input_i_o(input_list=input_list)
    if result == 502:
        st.write("کالایی که قصد حذف آن را داشتید در انبار موجود نبود و عملیات شما صورت نگرفت")
    st.rerun()
    submit = None
    # send input list then clear submit
    