import streamlit as st
from Engin import back_finance

def main_bio():
    _, col2, _ = st.columns(3)
    with col2:
        st.write("# :مجموع دارایی")
    col1, _, col3 = st.columns(3)
    with col1:
        st.write("### :دارایی حاصل از کالا")
    with col3:
        st.write("### :دارایی نقدی")



def main():
    main_bio()

main()
    
