import streamlit as st

def bar():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "level_account" not in st.session_state:
        st.session_state.level_account = None
    
    login_page = st.Page("account\login_page.py", title="Log in", icon=":material/login:")
    logout_page = st.Page("account\logout_page.py", title="Log out", icon=":material/logout:")
    Person_page = st.Page("account/Person_account.py", title="حساب کاربری")

    warehouse = st.Page("انبار\موجودی انبار.py", title="موجودی انبار", default=True)
    i_o = st.Page("انبار\ورودی و خروجی.py", title="ورودی و خروجی")
    products = st.Page("انبار\محصولات.py", title="محصولات")
    
    lend = st.Page("امانات\امانت.py", title="امانت")
    persons = st.Page("امانات\مخاطبین.py", title="مخاطبین")
    
    finance = st.Page("حسابداری\حسابداری.py", title="حسابداری")
    
    if st.session_state.logged_in:
        print(st.session_state.level_account)
        page = st.navigation(
                {
                    "انبار": [warehouse, i_o, products],
                    "امانات": [lend, persons],
                    "حسابداری": [finance],
                    "حساب کاربری": [Person_page, logout_page]
                },
                position="sidebar"
            )
    else:
        page = st.navigation(
                {
                    "حساب کاربری": [login_page]
                }
            )

    page.run()
    
def main():
    bar()

main()