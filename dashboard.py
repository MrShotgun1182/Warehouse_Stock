import streamlit as st

def bar():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "level_account" not in st.session_state:
        st.session_state.level_account = None
    
    login_page = st.Page("accont\login_page.py", title="Log in", icon=":material/login:")
    logout_page = st.Page("accont\logout_page.py", title="Log out", icon=":material/logout:")

    warehouse = st.Page("انبار\موجودی انبار.py", title="موجودی انبار", default=True)
    i_o = st.Page("انبار\ورودی و خروجی.py", title="ورودی و خروجی")
    products = st.Page("انبار\محصولات.py", title="محصولات")
    
    lend = st.Page("امانات\امانت.py", title="امانت")
    persons = st.Page("امانات\مخاطبین.py", title="مخاطبین")
    
    finance = st.Page("حسابداری\حسابداری.py", title="حسابداری")
    
    if st.session_state.logged_in:
        page = st.navigation(
                {
                    "حساب کاربری": [logout_page],
                    "انبار": [warehouse, i_o, products],
                    "امانات": [lend, persons],
                    "حسابداری": [finance]
                },
                position="sidebar"
            )
    else:
        page = st.navigation(
                {
                    "حسباکاربری": [login_page]
                }
            )

    page.run()
    
def main():
    bar()

main()