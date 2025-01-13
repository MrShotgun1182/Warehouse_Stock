import streamlit as st
from Engine import back_person as bp

def person_DF():
    st.set_page_config(page_title="افراد")
    
    st.write("# :لیست افراد")

    st.dataframe(back.make_person_DF(), use_container_width=True, selection_mode="multi-row")

def new_person():
    st.write("# :افزودن فرد جدید")

    with st.form("New_Person"):
        col1, col2 = st.columns(2)
        
        with col1:
            name_lastname = st.text_input(label="نام و نام خانوادگی", placeholder="اجباری")
        
        with col2: 
            phon_number = st.number_input(label="شماره تلفن", placeholder="شماره تلفن", value=None, step=1)
            
        Information = st.text_input(label="اطلاعات", placeholder="اختیاری")
        submit = st.form_submit_button("ثبت", use_container_width=True)

    if submit:
        input_list = [name_lastname, phon_number, Information]
        back.input_peron(input_list)
        submit = None

def update_person():
    st.write("# :تغییر اطلاعات فرد")

    with st.form("Update_Person"):
        personID = st.number_input(label="کد فرد را وارد کنید", placeholder="اجباری", step=1)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name_lastname = st.text_input(label="نام و نام خانوادگی", placeholder="*")
        
        with col2: 
            phon_number = st.number_input(label="شماره تلفن", placeholder="شماره تلفن", value=None, step=1)

        Information = st.text_input(label="اطلاعات", placeholder="*")
        submit = st.form_submit_button("ثبت", use_container_width=True)

    if submit:
        input_list = [personID, name_lastname, phon_number, Information]
        back.update_person(input_list)
        submit = None

def search():
    with st.form("search by name"):
        name = st.text_input("جست و جو", placeholder="نام فرد را وارد کنید")
        submit = st.form_submit_button("جست و جو")
        if submit:
            input_dic = {
                "name": name
            }
            search_DF = back.search_by_name(input_dic)
            st.dataframe(search_DF, use_container_width=True)

def main():
    if st.session_state.level_account in ["admin", "operator", "spectator"]:
        person_DF()
        search()
        if st.session_state.level_account in ["admin", "operator"]:
            new_person()
        if st.session_state.level_account == "admin":
            update_person()
    
back = bp()    
main()
