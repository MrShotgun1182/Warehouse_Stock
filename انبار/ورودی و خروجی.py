import streamlit as st
from Engine import back_i_o, dic_date, make_dic

def header():
    st.set_page_config(page_title="i_o")
    st.write("<div style='text-align: center'> <h1> ورودی و خروجی انبار <h1> </div>", unsafe_allow_html=True)
    
def i_o_DF():
    st.write("<div style='text-align: center'> <h4> :جدول ورودی و خروجی انبار<h4> </div>", unsafe_allow_html=True)
    
    st.dataframe(back.make_i_o_DF(), use_container_width=True, selection_mode="multi-row")

    st.divider()

def add_i_o():
    
    st.write("<div style='text-align: center'> <h4>افزودن داده جدید<h4> </div>", unsafe_allow_html=True)
    with st.form('myform'):
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            i_oType = st.radio('ورودی / خروجی', options=['ورودی', 'خروجی'])
            
        with col2:
            ProductName = st.selectbox("نام کالا", list(make_dic("Products").values()), placeholder='*')
            
        with col3:
            Number = st.number_input(label="تعداد", placeholder='*', step=1, min_value=1, value=1)
            submit = st.form_submit_button("درج کردن")
            
        with col4: 
            Pric = st.number_input(label="(تومان)قیمت هر واحد", placeholder='*', step=1, min_value=1)     
            
        with col5:
            date = dic_date()
            date = st.text_input(label="تاریخ", value=date, placeholder=date)
        

    if submit:
        input_list = [i_oType, ProductName, Pric, Number, date]
        result = back.input_i_o(input_list=input_list)
        if result == 502:
            st.write("کالایی که قصد حذف آن را داشتید در انبار موجود نبود و عملیات شما صورت نگرفت")
        st.rerun()
        submit = None
    
def main():
    header()
    i_o_DF()
    add_i_o()
    
back = back_i_o()
main()