import sqlite3

class MySQLiteDB():
    def __init__(self):
        self.connect_to_db()
        self.cur = self.db.cursor()
        self.create_table()
   
    def connect_to_db(self):
        try:
           self.db = sqlite3.connect("test.db")
           print("database is created")
        except:
           print("Fail to create database")
           self.db.close()
    
    def create_table(self):
        try:
            self.cur.execute(""" 
                CREATE TABLE Testy (
                    hours_number REAL,
                    word_date DATE
                )
                """)
            print("Tabel is created")
            
        except sqlite3.OperationalError:
            print("Tabela już istnieje")
            
    
    def insert_data(self, my_hours, my_date):
        print(f"{my_hours =} {type(my_hours)}")
        print(f"{my_date =} , {type(my_date)}")
        query = f"""INSERT INTO Testy (hours_number, word_date)
                    VALUES ({my_hours}, '{my_date}')"""
        print(query)
        self.cur.execute(query)
        self.db.commit()
        print("Data inserted")
        




if __name__=="__main__":
    my_db = MySQLiteDB()

