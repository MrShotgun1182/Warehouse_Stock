import streamlit as st

def header():
    st.set_page_config(page_title="login page")


def login():
    st.write("its login page")
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def main():
    login()

main()