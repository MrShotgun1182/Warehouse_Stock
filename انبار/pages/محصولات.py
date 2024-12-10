import streamlit as st
from Engin import back_products as bp

back = bp()

st.set_page_config(page_title="محصولات")

st.write("# :لیست کالاهای")

st.dataframe(back.make_products_DF(), use_container_width=True, selection_mode="multi-row")

st.write("# :افزودن کالا جدید")

with st.form('form_product'):
    col1 , col2, col3 = st.columns(3)
    
    with col1:
        product_name = st.text_input(label="نام کالا", placeholder='*')
    
    with col2:
        product_type = st.radio(label='کالا / دارایی', options=['کالا', 'دارایی'])
        submit = st.form_submit_button("درج کردن")

    with col3:
        description = st.text_input(label="توضیحات", placeholder='*')

if submit:
    input_list = [product_name, product_type, description]
    st.write(input_list)
    result = back.input_product(input_list)
    submit = None