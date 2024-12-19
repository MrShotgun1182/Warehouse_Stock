import pyodbc as odbc
import pandas as pd
class SQL:
    __connect__ = False
    SERVER_NAME = '.'
    DATABASE_NAME = "barbita"
    USERNAME = 'sa' 
    PASSWORD = 'admin@2024'
    def __init__(self):
        connectionString = f'DRIVER={{SQL SERVER}};SERVER={self.SERVER_NAME};DATABASE={self.DATABASE_NAME}'
        if self.USERNAME and self.PASSWORD:
            connectionString += f';UID={self.USERNAME};PWD={self.PASSWORD}'
        try:
            self.conn = odbc.connect(connectionString)
            self.cursor = self.conn.cursor()
            self.__connect__ = True
        except:
            self.__connect__ = False
        
    def add_Product(self, ProductName, Description = None):
        if Description:
            query = F"""INSERT INTO Products (ProductName, Description)
            VALUES (N'{ProductName}', N'{Description}');"""
        else:
            query = F"""INSERT INTO Products (ProductName)
            VALUES (N'{ProductName}');"""
            
        self.cursor.execute(query)
        self.conn.commit()
        
    def add_Person(self, Name_Lastname, Phonnumber, Information):
        if Information == None:
            query = F"""
                INSERT INTO Persons (Name_Lastname, PhonNumber)
                VALUES (N'{Name_Lastname}', '{Phonnumber}');"""
        else:
            query = F"""
                INSERT INTO Persons (Name_Lastname, PhonNumber, Information)
                VALUES (N'{Name_Lastname}', '{Phonnumber}', N'{Information}');"""
            
        self.cursor.execute(query)
        self.conn.commit()
    
    def add_Lend(self, PersonID, ProductID, GiveLend, Numbers, GetLend = None, Description = None):
        if Description:
            if GetLend:
                query = F"""INSERT INTO Lend (PersonID, ProductID, GiveLend, Numbers, GetLend, Description)
                        VALUES ('{PersonID}', '{ProductID}', '{GiveLend}', '{Numbers}', '{GetLend}', N'{Description}');"""
            else:
                query: F"""INSERT INTO Lend (PersonID, ProductID, GiveLend, Numbers, Description)
                        VALUES ('{PersonID}', '{ProductID}', '{GiveLend}', '{Numbers}', N'{Description}');"""
        else:
            if GetLend:
                query = F"""INSERT INTO Lend (PersonID, ProductID, GiveLend, Numbers, GetLend)
                        VALUES ('{PersonID}', '{ProductID}', '{GiveLend}', '{Numbers}', '{GetLend}');"""
            else:
                query = F"""INSERT INTO Lend (PersonID, ProductID, GiveLend, Numbers)
                        VALUES ('{PersonID}', '{ProductID}', '{GiveLend}', '{Numbers}');"""
                
        self.cursor.execute(query)
        self.conn.commit()
        
    def add_i_o(self, i_oType, ProductID, Price, Date, Number):
        query = F"""
            INSERT INTO i_o (i_oType, ProductID, Price, Date, Number)
            VALUES ('{i_oType}', '{ProductID}', '{Price}', '{str(Date)}', '{Number}');"""
            
        self.cursor.execute(query)
        self.conn.commit()
        
    def add_Warehouse_Stock(self, ProductID, WS_Inventory):
        query = F"""
            INSERT INTO Warehouse_Stock (ProductID, WS_Inventory)
            VALUES ('{ProductID}', '{WS_Inventory}');
        """
        self.cursor.execute(query)
        self.conn.commit()
     
    def update_Warehouse_Stock(self, WSID, WS_Inventory):
        query = f"""UPDATE Warehouse_Stock
                SET WS_Inventory = {WS_Inventory}
                WHERE WSID = {WSID};"""
                
        self.cursor.execute(query)
        self.conn.commit()
        
    def update_Lend(self, LendID, Get_lend):
        query = f"""UPDATE Lend
                SET GetLend = '{Get_lend}'
                WHERE LendID = {LendID};"""
                
        self.cursor.execute(query)
        self.conn.commit()
        
    def update_Product(self, Product_ID , Product_name, Description):
        query = f"""UPDATE Products
                SET ProductName = N'{Product_name}', Description = N'{Description}'
                WHERE ProductID = {Product_ID};"""
                
        self.cursor.execute(query)
        self.conn.commit()
        
    def update_Person(self, Person_ID, Person_name, PhonNumber, Information):
        if Information == None:
            query = f"""UPDATE Persons
                    SET Name_Lastname = N'{Person_name}', PhonNumber = '{PhonNumber}'
                    WHERE PersonID = {Person_ID}"""
        else:
            query = f"""UPDATE Persons
                    SET Name_Lastname = N'{Person_name}', PhonNumber = '{PhonNumber}', Information = N'{Information}'
                    WHERE PersonID = {Person_ID}"""
        
        self.cursor.execute(query)
        self.conn.commit()
        
    def get_table(self, Table_Name):
        query = f"""SELECT * FROM dbo.{Table_Name}"""

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
        
    def gat_column_name(self, Table_name):
        query = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{Table_name}'"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def delet_row(self, Table_name, Column_name, ID):
        query = f"""DELETE FROM {Table_name} WHERE {Column_name} = {ID};"""
        
        self.cursor.execute(query)
        self.conn.commit()
    
    def get_target_row_WS(self, ProductID):
        query = f"""SELECT * FROM  dbo.Warehouse_Stock WHERE ProductID = {ProductID}"""

        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            result = list()
            for i in data[0]:
                result.append(i)
            return result
        except:
            return None
    
    def Current_loan_data(self):
        query = F"""select * from Lend where GetLend is null"""

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
if __name__ == "__main__":
    # try: 
    test = SQL()
    # test.add_Product(ProductName="سلام")
    # print(test.get_target_row_WS(ProductID=1003))
    # test.add_i_o(i_oType=0, ProductID=1004, Price=21, Date=12334, Number=4)
    # print(test.get_target_row_WS(ProductID=1003))
    # print(test.gat_column_name("Warehouse_stock"))
    # print(test.get_table("Warehouse_stock"))
    # data=test.get_table("Warehouse_stock")
    # print(pd.DataFrame.to_sql(data= data))
    # test.add_Product(ProductName="s1", ProductType="1", Description="سلام داداش خوبی شما")
    print("ok")
    # except Exception as err:
    #     print(err)
    #     print("not ok")