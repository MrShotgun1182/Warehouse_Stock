import streamlit as st
from Engine import back_Person_account

def header():
    st.set_page_config(page_title="حساب کاربری")
    st.write("<div style='text-align: center'> <h1>حساب کاربری<h1> </div>", unsafe_allow_html=True)
    st.divider()

def account_bio():
    col1, _, col3 = st.columns(3)

    with col1:
        st.write(":سطح دسترسی")
        st.write(st.session_state.level_account)
    
    with col3:
        st.write(":نام کاربری")
        st.write(st.session_state.user_name)
    
    st.divider()

def new_account():
    # with st.exception("افزودن حساب جدید"):
    with st.form("new_account", border=True):
        
        col1 , col2= st.columns(2)
        with col1:
            user_name = st.text_input(label="نام کاربری", placeholder="اجباری")

        with col2:
            level = st.selectbox(label="سطح دسترسی", options=["بازدید کننده", "کاربر","ادمین"])
        
        passwor = st.text_input(label="رمز عبور", placeholder="اجباری", type="password")
        true_password = st.text_input(label="تکرار رمز عبور", placeholder="اجباری", type="password")
        submit = st.form_submit_button("افزودن کاربر", use_container_width=True)
    
        if submit:
            if back.test_password(password=passwor, true_password=true_password):
                input_dic = {
                    "user_name": user_name,
                    "password": passwor,
                    "level": level
                }
                back.input_User(input_dic=input_dic)
                st.write(back.__add_user__)
            else:
                st.write("رمز عبور را دوباره وارد کنید")


def main():
    if st.session_state.level_account in ["admin", "operator", "spectator"]:
        header()
        account_bio()
        if st.session_state.level_account == "admin":
            new_account()

back = back_Person_account()
main()