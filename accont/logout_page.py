import streamlit as st

def logout():
    if st.button("Log out", ):
        st.session_state.logged_in = False
        st.rerun()

def main():
    logout()

main()