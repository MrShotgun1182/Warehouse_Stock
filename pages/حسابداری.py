import streamlit as st
from Engin import back_finance
from Engin import dic_date

def header():
    st.set_page_config(page_title="Information")
    _, col2, _ = st.columns(3)
    with col2:
        st.write("# :حسابداری")
        
    
def forms():
    date = dic_date()
    col_form1, col_form2 = st.columns(2)
    with col_form1:
        with st.expander("برداشت از حساب"):
            with st.form("accont_picke", border=False):
                form1_col1, form1_col2 = st.columns(2)
                with form1_col1:
                    price = st.number_input(label=":مبلغ برداشت", step=1)
                with form1_col2:
                    date = st.text_input(label=":تاریخ برداشت", placeholder=date, value=date)
                information = st.text_input(label=":شرح برداشت", placeholder="اجباری")
                description = st.text_input(label=":توضیحات", placeholder="اختیاری")
                submit_fomr1 = st.form_submit_button("ثبت", use_container_width=True)
    
                if submit_fomr1:
                    input_dic = {
                        "type": 1,
                        "price": price,
                        "date": date,
                        "information": information,
                        "description": description
                    }
                    
                    st.write(F"""{input_dic["price"]} :مبلغ برداشت از حساب""")
                    st.write(F"""{input_dic["date"]} :تاریخ برداشت از حساب""")
                    st.write(F"""{input_dic["information"]} :شرح برداشت از حساب""")
                    back.input_finance(input_dic=input_dic)
                    st.write(back.__add_finance__)
                    submit_fomr1 = None

        
    with col_form2:
        with st.expander("واریز به حساب"):
            with st.form("accont_deposit", border=False):
                form1_col1, form1_col2 = st.columns(2)
                with form1_col1:
                    price = st.number_input(label=":مبلغ واریز", step=1)
                with form1_col2:
                    date = st.text_input(label=":تاریخ واریز", placeholder=date, value=date)
                information = st.text_input(label=":شرح واریز", placeholder="اجباری")
                description = st.text_input(label=":توضیحات", placeholder="اختیاری")
                submit_form2 = st.form_submit_button("ثبت", use_container_width=True)
                
                if submit_form2:
                    input_dic = {
                        "type": 0,
                        "price": price,
                        "date": date,
                        "information": information,
                        "description": description
                    }
                    st.write(F"""{input_dic["price"]} :مبلغ واریز به حساب""")
                    st.write(F"""{input_dic["date"]} :تاریخ واریز به حساب""")
                    st.write(F"""{input_dic["information"]} :شرح واریز به حساب""")
                    back.input_finance(input_dic=input_dic)
                    st.write(back.__add_finance__)
                    submit_form2 = None



def main():
    header()
    forms()

back = back_finance()
main()
    
