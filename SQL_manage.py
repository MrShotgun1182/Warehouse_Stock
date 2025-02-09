import pyodbc as odbc

class SQL:
    __connect__ = False
    SERVER_NAME = '.'
    DATABASE_NAME = "Barbita"
    USERNAME = None
    PASSWORD = None
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
            VALUES ({ProductID}, {WS_Inventory});
        """
        self.cursor.execute(query)
        self.conn.commit()
    
    def add_finance(self, Type, Price, Date, Information, Description = None):
        if Description:
            query = F"""INSERT INTO Finance (Type, Price, Date, Information, Description)
            VALUES ({Type}, {Price}, '{Date}', N'{Information}', N'{Description}');"""
        else:
            query = F"""INSERT INTO Finance (Type, Price, Date, Information)
            VALUES ({Type}, {Price}, '{Date}', N'{Information}');"""
        
        self.cursor.execute(query)
        self.conn.commit()
    
    def add_user(self, user_name, password, level, creat_account):
        query = F"""INSERT INTO Users (User_name, Password, Level, Creat_account)
            VALUES ('{user_name}', '{password}', '{level}', '{creat_account}');"""
        
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
        
    def delete_row_by_ID(self, Table_Name,ID_column_name, value):
        query = F"""DELETE FROM {Table_Name} WHERE {ID_column_name} = {value};"""

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
    
    def finance_month(self, month):
        query = F"""SELECT * FROM Finance WHERE Date LIKE '%/{month}/%'"""

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def find_account(self, user_name, password):
        query = F"""SELECT Level FROM Users WHERE User_name = '{user_name}' and password = '{password}'"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return 
        
    def search_person(self, name):
        query = F"""SELECT * FROM Persons WHERE Name_Lastname LIKE N'%{name}%' """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_one_column(self, Table_name, Column_name):
        query = F"""SELECT {Column_name} FROM {Table_name}"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

if __name__ == "__main__":
    test = SQL()
    print(test.finance_month(9))
