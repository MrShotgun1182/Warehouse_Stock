import streamlit as st
from Engine import back_login_page

def header():
    st.set_page_config(page_title="login page")

def login_form():
    with st.form("login_form"):
        user_name = st.text_input(label="نام کاربری خود را وارد کنید")
        password = st.text_input(label="رمز عبور خود را وارد کنید", type="password")
        submit = st.form_submit_button(label="ورود", use_container_width=True)

    if submit:
        input_dic = {
            "user_name": user_name,
            "password": password
        }
        account_status = back.test_account(input_dic)
        if account_status == 200:
            st.session_state.level_account = back.__level_account__
            st.session_state.user_name = user_name
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.write(back.__account_status__)

def main():
    header()
    login_form()

back = back_login_page()
main()