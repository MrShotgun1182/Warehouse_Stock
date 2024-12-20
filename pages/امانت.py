import streamlit as st
from Engin import back_lend as bl
from Engin import make_dic, dic_date

def lend_DF():
    st.set_page_config(page_title="امانت")
    
    st.write("# :لیست امانت")

    st.dataframe(back.make_lend_DF(), use_container_width=True)
    
def new_lend():
    st.write("#  اضافه کردن امانت")

    with st.form("New_Lend"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            person_name = st.selectbox(label="نام گیرنده امانت", options=list(make_dic("Persons").values()), placeholder="اجباری")
            
        with col2:
            product_name = st.selectbox(label="نام کالا", options=list(make_dic("Products").values()), placeholder="اجباری")
        
        with col3:
            numbers = st.number_input(label="تعدادامانت", step=1, placeholder="اجباری")
    
        column1, column2 = st.columns(2)
        
        with column1:
            date = dic_date()
            give_lend = st.text_input(label="تاریخ دریافت امانت", value=date, placeholder=date)
            
        with column2:
            get_lend = st.text_input(label="تاریخ بازگشت امانت", placeholder="اختیاری")
        
        description = st.text_input(label="توضیحات", placeholder="اختیاری")
        submit = st.form_submit_button("درج کردن")
        
    if submit:
        input_list = [person_name, product_name, numbers, give_lend, get_lend, description]
        back.input_lend(input_list)
        st.write(input_list)
        st.write(back.__add_lend__)
        submit = None
        
def current_loan():
    st.write("# :امانت های جاری")
    
    st.dataframe(back.Current_loan_DF(), use_container_width=True)


def main():
    lend_DF()
    new_lend()
    current_loan()
    
back = bl()
main()