from SQL_manage import SQL
import pandas as pd
import jdatetime
import hashlib

def dic_date():
    date = jdatetime.datetime.now()
    dic_date = f"""{date.year}/{date.month}/{date.day}"""

    return dic_date

def make_dic(Table_name): 
    obj = SQL()
    data = obj.get_table(Table_name)
    dic = {}
    for row in data:
        dic[row[0]] = row[1]
    return dic # dic = {ID: name}

class back_WS():
    def make_WS_DF(self):
        Table_name = "Warehouse_stock"
        obj = SQL()
        data = obj.get_table(Table_name)
        dic = make_dic("Products")
        DF_list = []
        for row in data:
            # print(row)
            DF_dic = {
                "کد موجود در انبار": row[0],
                "کد کالا": str(row[1]),
                "نام کالا": dic[row[1]],
                "موجودی در انبار": row[2]
            }
            DF_list.append(DF_dic)
            
        DF = pd.DataFrame(DF_list)
        return DF

class back_i_o:    
    def make_i_o_DF(self):
        Table_name = "i_o"
        obj = SQL()
        data = obj.get_table(Table_name)
        dic = make_dic("Products")
        DF_list = []
        for row in data:
            DF_dic = {
                "شماره ورودی و خروجی": row[0],
                "نوع": "ورود" if row[1] == 0 else "خروجی",
                "نام کالا": dic[row[2]],
                "قیمت هر واحد": row[3],
                "تعداد": row[5],
                "قیمت کل": row[5] * row[3],
                "تاریخ": row[4]
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
    
    def input_i_o(self, input_list):
        dic = make_dic("Products")
        for key, value in dic.items():
            if value == input_list[1]:
                input_list[1] = key
        
        if input_list[0] == "ورودی":
            input_list[0] = 0
        else:
            input_list[0] = 1
            
        obj = SQL()
        
        # update WS
        row = obj.get_target_row_WS(ProductID= input_list[1])
        if input_list[0] == 0:
            if row != None:
                new_WS_Inventory = row[2] + input_list[3]
                obj.update_Warehouse_Stock(WSID=row[0], WS_Inventory=new_WS_Inventory)
            else:
                obj.add_Warehouse_Stock(ProductID=input_list[1] , WS_Inventory=input_list[3])
        else:
            if row != None:
                new_WS_Inventory = row[2] - input_list[3]
                if new_WS_Inventory <= 0:
                    obj.delet_row(Table_name="Warehouse_Stock", Column_name="WSID", ID=row[0])
                else:
                    obj.update_Warehouse_Stock(WSID=row[0], WS_Inventory=new_WS_Inventory)
            else:
                return 502
        obj.add_i_o(i_oType=input_list[0], ProductID=input_list[1], Price=int(input_list[2]), Date=str(input_list[4]), Number=int(input_list[3]))
        return 200

class back_products:
    __add_product__ = 'کالا جدیدی ثبت نشده است'
    __update_product__ = ""
    __delete_status__ = ""
    
    def make_products_DF(self):
        Table_name = "Products"
        obj = SQL()
        data = obj.get_table(Table_Name=Table_name)
        DF_list = list()
        for row in data:

            DF_dic = {
                "کد کالا": str(row[0]),
                "نام کالا": row[1],
                "توضیحات": "" if row[2] == None else row[2],
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        DF["کد کالا"] = DF["کد کالا"].str.replace(',', '')
        return DF
    
    def input_product(self, input_list):
        dic = make_dic("Products")
        if input_list[0] == "":
            self.__add_product__ = "نام کالا را وارد کنید"
            return 501
        if input_list[0] in dic.values():
            self.__add_product__ = "این کالا قبلا ثبت شده است"
            return 501
        
        obj = SQL()
        obj.add_Product(ProductName=input_list[0], Description=input_list[1])
        self.__add_product__ = "کالا جدید ثبت شد"
        return 200

    def update_product(self, input_lsit):
        dic = make_dic("Products")

        if not input_lsit[0] in dic.keys():
            self.__update_product__ = "کد کالا یافت نشد"

        obj = SQL()
        obj.update_Product(Product_ID=input_lsit[0], Product_name=input_lsit[1], Description=input_lsit[2])
        self.__update_product__ = F"کالا با شماره{input_lsit[0]}بروزرسانی شد"        

    def delete_prooduct(self, input_dic):
        if input_dic["productID"] == "":
            self.__delete_status__ = "کد کالا الزامی است"
            return 500

        obj = SQL()
        
        data_in_stack = obj.get_one_column(Table_name="Warehouse_stock", Column_name="ProductID")
        in_stack = list()
        for row in data_in_stack:
            in_stack.append(row[0])
        if input_dic["productID"] in in_stack:
            self.__delete_status__ = "این کالا در انبار موجود است"
            return 500
        
        data_in_i_o = obj.get_one_column(Table_name="i_o", Column_name="ProductID")
        in_i_o = list()
        for row in data_in_i_o:
            in_i_o.append(row[0])
        if input_dic["productID"] in in_i_o:
            self.__delete_status__ = "کالا در لیست ورودی و خروجی ثبت شده است"
            return 500
        
        obj.delete_row_by_ID(Table_Name="Products", ID_column_name="ProductID", value=input_dic["productID"])
        return 200

class back_person:
    __add_person__ = "فرد جدیدی ثبت نشده"
    __update_person__ = "بروزرسانی نداشته اید"
    __search_person__ = "جست و جویی وارد نشده"
    
    def make_person_DF(self):
        Table_name = "Persons"
        obj = SQL()
        data = obj.get_table(Table_Name=Table_name)
        DF_list = list()
        for row in data:
            
            DF_dic = {
                "کد فرد": row[0],
                "نام و نام خانوادگی افراد": row[1],
                "شماره تلفن": row[2],
                "اطلاعات": row[3]
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
    
    def input_peron(self, input_list):
        if input_list[0] == "":
            self.__add_person__ = "نام فرد وارد نشده"
            return 501
        if input_list[1] == None:
            self.__add_person__ = "شماره تلفن الزامی است"
            return 501
        if input_list[2] == "":
            input_list[2] = None
        
        obj = SQL()
        obj.add_Person(Name_Lastname=input_list[0], Phonnumber=input_list[1], Information=input_list[2])
        self.__add_person__ = "فرد جدید ثبت شد"
        return 200

    def update_person(self, input_list):
        if input_list[0] == None:
            self.__update_person__ = "کد فرد الزامی است"
            return 501
        if input_list[1] == "":
            self.__update_person__ = "نام فرد وارد نشده"
            return 501
        if input_list[2] == None:
            self.__update_person__ = "شماره تلفن الزامی است"
            return 501
        if input_list[3] == "":
            input_list[3] = None
        
        obj = SQL()
        obj.update_Person(Person_ID=input_list[0], Person_name=input_list[1], PhonNumber=input_list[2], Information=input_list[3])
        self.__update_person__ = "اطلاعات فرد بروزرسانی شد"
        return 200
            
    def search_by_name(self, input_dic):
        if input_dic["name"] == "":
            self.__search_person__ = "نام فرد الزامی است"
            return 500

        obj = SQL()
        data = obj.search_person(input_dic["name"])
        DF_list = list()
        for row in data:
            DF_dic = {
                "کد فرد": row[0],
                "نام و نام خانوادگی": row[1],
                "شماره تلفن": row[2],
                "اطلاعات": row[3]
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
            
class back_lend:
    __add_lend__ = "مورد جدیدی ثبت نشده"
    def make_lend_DF(self):
        Table_name = "Lend"
        obj = SQL()
        data = obj.get_table(Table_Name=Table_name)
        DF_list = list()
        person_dic = make_dic(Table_name="Persons")
        product_dic = make_dic(Table_name="Products")
        for row in data:
            DF_dic = {
                "کد امانت": row[0],
                "نام گیرنده امانت": person_dic[row[1]],
                "نام کالا امانت": product_dic[row[2]],
                "تاریخ دریافت امانت": row[3],
                "تعداد دریافتی": row[4],
                "تاریخ بازگشت": "کالا بازگشت نداشته" if row[5] == None else row[5],
                "توضیحات": row[6]
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
    
    def input_lend(self, input_list):
        input
        if input_list[0] == "":
            self.__add_lend__ = "نام شخص الزامی است"
            return 501
        if input_list[1] == "":
            self.__add_lend__ = "نام کالا الزامی است"
            return 501
        if input_list[2] == None:
            self.__add_lend__ = "تعداد الزامی است"
            return 501
        if input_list[3] == "":
            self.__add_lend__ = "تاریخ امانت دادن الزامی است"
            return 501

        if input_list[4] == "":
            input_list[4] = None
        if input_list[5] == "":
            input_list[5] = None
            
        dic_person = make_dic(Table_name="Persons")
        dic_product = make_dic(Table_name="Products")

        for key, value in dic_person.items():
            if value == input_list[0]:
                input_list[0] = key
                
        for key, value in dic_product.items():
            if value == input_list[1]:
                input_list[1] = key
        
        obj = SQL()
        
        #update WS
        row = obj.get_target_row_WS(ProductID=input_list[1])
        if row != None:
            new_WS_Inventory = row[2] - input_list[2]
            if new_WS_Inventory > 0:
                obj.update_Warehouse_Stock(WSID=row[0], WS_Inventory=new_WS_Inventory)
                
            elif new_WS_Inventory == 0:
                obj.delet_row(Table_name="Warehouse_Stock", Column_name="WSID", ID=row[0])
            else:
                self.__add_lend__ = "موجودی انبار کافی نیست"
                return 501
        else:
            self.__add_lend__ = "در انبار کالا مورد نظر موجود نیست"
            return 501
        
        obj.add_Lend(PersonID=input_list[0], ProductID=input_list[1], GiveLend=input_list[3], Numbers=input_list[2], GetLend=input_list[4], Description=input_list[5])
        self.__add_lend__ = "داده جدید ثبت شد"
        return 200
        
    def Current_lend_DF(self):
        obj = SQL()
        data = obj.Current_loan_data()
        DF_list = list()
        person_dic = make_dic(Table_name="Persons")
        product_dic = make_dic(Table_name="Products")
        for row in data:
            DF_dic = {
                "کد امانت": row[0],
                "نام گیرنده امانت": person_dic[row[1]],
                "نام کالا امانت": product_dic[row[2]],
                "تاریخ دریافت امانت": row[3],
                "تعداد دریافتی": row[4],
                "تاریخ بازگشت": "کالا بازگشت نداشته" if row[5] == None else row[5],
                "توضیحات": row[6],
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
                 
class back_finance:
    __add_finance__ = "حساب جدیدی ثبت نشده"

    def finance_DF(self):
        Table_name = "Finance"
        obj = SQL()
        data = obj.get_table(Table_Name=Table_name)
        DF_list = list()
        for row in data:
            DF_dic = {
                "کد تراکنش": row[0],
                "نوع تراکنش": "واریز" if row[1] == 0 else "برداشت",
                "مبلغ": row[2],
                "تاریخ": row[3],
                "شرح تراکنش": row[4],
                "توضیحات": row[5]
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        return DF
    
    def input_finance(self, input_dic):
        if input_dic["price"] == 0:
            self.__add_finance__ = "مبلغ الزامی است"
            return 500
        elif input_dic["date"] == "":
            self.__add_finance__ = "تاریخ الزامی است"
            return 500
        elif input_dic["information"] == "":
            self.__add_finance__ = "فیلد شرح الزامی است"
            return 500
        
        if input_dic["description"] == "":
            input_dic["description"] = None
            
        obj = SQL()
        obj.add_finance(Type=input_dic["type"], Price=input_dic["price"], Date=input_dic["date"], Information=input_dic["information"], Description=input_dic["description"])
        self.__add_finance__ = "داده جدید ثبت شد"
        return 200

    def sum_pike_deposit_month(self, month):
        obj = SQL()
        data = obj.finance_month(month=month)
        pike, deposit = 0, 0
        for row in data:
            if row[1] == 1:
                pike += row[2]
            else:
                deposit += row[2]
        return deposit, pike

class back_login_page:
    __account_status__ = "خارج از حساب کاربری"
    __level_account__ = "no level"
    def test_account(self, input_dic):
        if input_dic["user_name"] == None:
            self.__account_status__ = "نام کاربری را وارد کنید"
            return 500
        if input_dic["password"] == None:
            self.__account_status__ = "رمز عبور را وارد کنید"
            return 500
        
        bytes_password = bytes(input_dic["password"], "utf-8")
        Hash_password = hashlib.sha256(bytes_password).hexdigest()

        obj = SQL()
        level_account = obj.find_account(user_name=input_dic["user_name"], password=Hash_password)

        if not level_account:
            self.__account_status__ = "نام کاربری یا رمز عبور اشتباه است"
            return 500

        self.__level_account__ = level_account[0][0]
        return 200

class back_Person_account:
    __add_user__ = "اکانت جدیدی ثبت نشده است"
    def input_User(self, input_dic):
        if input_dic["user_name"] == None:
            self.__add_user__ = "نام کاربری اجباری است"
            return 500
        if input_dic["password"] == None:
            self.__add_user__ = "رمز عبور اجباری است"
            return 500
        if input_dic["level"] == None:
            self.__add_user__ = "سطح دسترسی را انتخاب کنید"
            return 500

        bytes_password = bytes(input_dic["password"], "utf-8")
        Hash_password = hashlib.sha256(bytes_password).hexdigest()

        if input_dic["level"] == "ادمین":
            level = "admin"
        elif input_dic["level"] == "کاربر":
            level = "operator"
        else:
            input_dic["level"] == "بازدید کننده"
            level = "spectator"

        date = dic_date()

        obj = SQL()
        obj.add_user(user_name=input_dic["user_name"], password=Hash_password, level=level, creat_account=date)
        self.__add_user__ = "حساب جدید ایجاد شد"
        return 200

    def test_password(self, password, true_password):
        if password == true_password:
            return True
        else:
            return False


if __name__ == "__main__":
    test = back_products()
    print(test.delete_prooduct({"productID": 1026}))
    print(test.__delete_status__)
    # for row in make_dic("Warehouse_stock"):
    #     print(row)
    # print(make_dic("Warehouse_stock"))