import streamlit as st

st.set_page_config(page_title="main", page_icon="😊")
# custom_css = """
#         <div style='background-color: #43d448; padding: 10px; border-radius: 5px;'>
#     <h1>This is a header with background color</h1>
#     <p>This is some text inside a div with background color.</p>
# </div>"""
# st.markdown(custom_css, unsafe_allow_html=True)

st.write("# به سامانه انبار داری باربیتا خوش آمدید")

st.sidebar.success("بخش مورد نظر خود را انتخاب کنید")

st.markdown("""# demo mode""")

@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")

email_form()
