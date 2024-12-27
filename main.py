import streamlit as st

def header():
    st.set_page_config(page_title="main", page_icon="😊")
    # custom_css = """
    #         <div style='background-color: #43d448; padding: 10px; border-radius: 5px;'>
    #     <h1>This is a header with background color</h1>
    #     <p>This is some text inside a div with background color.</p>
    # </div>"""
    # st.markdown(custom_css, unsafe_allow_html=True)

    st.write("# به سامانه انبار داری باربیتا خوش آمدید")
    st.markdown("""# demo mode""")

def sidebar():
    st.sidebar.success("بخش مورد نظر خود را انتخاب کنید")
    
# @st.dialog("Sign up")
# def email_form():
#     name = st.text_input("Name")
#     email = st.text_input("Email")

# email_form()

def bar():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    def login():
        if st.button("Log in"):
            st.session_state.logged_in = True
            st.rerun()

    def logout():
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()
    
    login_page = st.Page(login, title="Log in", icon=":material/login:")
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

    # dashboard = st.Page(
    # "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
    # )
    
    lend = st.Page("امانات\امانت.py", title="امانت", default=True)

    if st.session_state.logged_in:
        page = st.navigation(
                {
                    "حساب کاربری": [logout_page],
                    "امانات": [lend]
                }
            )

def main():
    header()
    # sidebar()
    bar()

main()