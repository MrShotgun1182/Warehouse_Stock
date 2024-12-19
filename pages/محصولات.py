import streamlit as st
from Engin import back_products as bp

def product_DF():
    st.set_page_config(page_title="محصولات")

    st.write("# :لیست کالاهای")

    st.dataframe(back.make_products_DF(), use_container_width=True, selection_mode="multi-row")

def new_product():
    st.write("# :افزودن کالا جدید")

    with st.form('New_Product'):
        col1 , col2, col3 = st.columns(3)
        
        with col1:
            product_name = st.text_input(label="نام کالا", placeholder='*')

        with col2:
            description = st.text_input(label="توضیحات", placeholder='*')
            
        with col3:
            submit = st.form_submit_button("درج کالا")
            st.markdown(f"###### {back.__add_product__}")

    if submit:
        input_list = [product_name, description]
        result = back.input_product(input_list)
        st.rerun()
        submit = None
    
def update_product():
    st.write("# :بروزرسانی")
    
    with st.form("Update_Product"):
        col1, col2= st.columns(2)
        
        with col1:
            product_ID = st.number_input(label="کد کالا را وارد کنید", step=1, value=1000)
        
        with col2:
            product_name = st.text_input(label="نام کالا")

        description = st.text_input(label="توضحیات")
        submit = st.form_submit_button("درج کردن", use_container_width=True)
        # st.write(f"##### {back.__update_product__}")
        
    if submit:
        input_list = [product_ID, product_name, description]
        result = back.update_product(input_list)
        st.rerun()
        submit = None
        
        
    
def main():
    product_DF()    
    new_product()
    update_product()
    
back = bp()
main()