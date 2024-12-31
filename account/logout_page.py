import streamlit as st

def logout():
    if st.button("Log out", ):
        st.session_state.logged_in = False
        st.session_state.level_account = None
        st.session_state.user_name = None
        st.rerun()

def main():
    logout()
    
main()