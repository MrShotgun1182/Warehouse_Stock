import streamlit as st

def login():
    st.write("its login page")
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def main():
    login()

main()