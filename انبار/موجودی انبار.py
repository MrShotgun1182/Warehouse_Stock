import streamlit as st
from Engine import back_WS

def header():
    st.set_page_config(page_title="WS")
    st.write("<div style='text-align: center'> <h1>موجودی انبار<h1> </div>", unsafe_allow_html=True)
    
def WS_DF():
    st.write("<div style='text-align: center'> <h4>:موجودی انبار به شرح زیر میباشد <h4> </div>", unsafe_allow_html=True)
    st.dataframe(back.make_WS_DF(), use_container_width=True, selection_mode="multi-row")
    
def main():
    header()
    WS_DF()
    
back = back_WS()
main()