import streamlit as st
from Engin import make_WS_DF

st.set_page_config(page_title="WS")

st.write("# :موجودی انبار به شرح زیر میباشد ")

st.dataframe(make_WS_DF(), use_container_width=True, selection_mode="multi-row")

