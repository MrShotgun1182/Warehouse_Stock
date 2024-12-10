from SQL_manage import SQL
import pandas as pd

def make_dic(Table_name): 
    obj = SQL()
    data = obj.get_table(Table_name)
    dic = {}
    for row in data:
        dic[row[0]] = row[1]
    # print(dic)
    return dic # dic = {ID: name}

def make_WS_DF():
    Table_name = "Warehouse_stock"
    obj = SQL()
    data = obj.get_table(Table_name)
    dic = make_dic("Products")
    DF_list = []
    for row in data:
        # print(row)
        DF_dic = {
            "کد موجود در انبار": row[0],
            "نام کالا": dic[row[1]],
            "موجودی در انبار": row[2]
        }
        DF_list.append(DF_dic)
        
    DF = pd.DataFrame(DF_list)
    return DF

def make_i_o_DF():
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

def input_i_o(input_list):
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
    print(row)
    print(type(row))
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

    def make_products_DF(self):
        Table_name = "Products"
        obj = SQL()
        data = obj.get_table(Table_Name=Table_name)
        DF_list = list()
        for row in data:
            if row[3] == None:
                row[3] = ""
            DF_dic = {
                "کد انبار کالا": str(row[0]),
                "نام کالا": row[1],
                "دارایی / کالا": row[2],
                "توضیحات": row[3],
            }
            DF_list.append(DF_dic)
        DF = pd.DataFrame(DF_list)
        DF["کد انبار کالا"] = DF["کد انبار کالا"].str.replace(',', '')
        return DF
    
    def input_product(self, input_list):
        dic = make_dic("Products")
        if input_list[0] == "":
            return "نام کالا را وارد کنید"
        if input_list[0] in dic.values():
            return "این کالا قبلا ثبت شده است"

if __name__ == "__main__":
    back = back_products()
    print(back.make_products_DF())
    # print(type(values[0]))
    # make_WS_DF()
    # make_i_o_DF()
    pass
    