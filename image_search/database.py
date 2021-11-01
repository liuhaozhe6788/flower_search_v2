import mysql.connector


myPassword = 'lfd6788'
myDatabase_name = 'flower_data'
myTables_name = ['flower_imgs']

class Database:

    # 私有变量初始化
    def __init__(self, mypassword, database_name=None, tables_name=[]):
        self._password = mypassword
        self._mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=self._password,
            database=database_name
        )
        self._mycursor = None
        self._database_name = database_name
        self._databases_list = None
        self._tables = tables_name
        self._tables_list_in_database = None
        self._mycursor = self._mydb.cursor(buffered=True)
        print("class initialized")

    def close(self):
        self._mydb.close()

    # 如果数据库不存在就创建该数据库，随后访问该数据库
    def access_database(self):
        self._mycursor.execute(f'create database if not exists {self._database_name}')
        self._mycursor.execute("show databases")
        self._databases_list = [x for x in self._mycursor]
        if self._database_name in self._databases_list:
            self._mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password=self._password,
                database=self._mydb
            )
            self._mycursor = self._mydb.cursor(buffered=True)

    # 创建表格
    def create_table(self, table_index):
        self._mycursor.execute(f"create table if not exists {self._tables[table_index-1]} (img_url varchar(255) primary key, \
                         result int unsigned, vector text) ")
        self._mycursor.execute("show tables")
        self._tables_list_in_database = [x for x in self._mycursor]

    def insert_row(self, table_index):
        pass

    def select(self):
        pass

    @property
    def databases(self):
        import copy
        return copy.deepcopy(self._databases_list)

    @property
    def tables(self):
        import copy
        return copy.deepcopy(self._tables_list_in_database)

    @property
    def data(self):
        import copy
        all_data = []
        for table_name in self._tables:
            self._mycursor.execute(f"select * from {table_name}")
            all_data.append(self._mycursor.fetchall())
        return copy.deepcopy(all_data)


if __name__ == "__main__":
    newDatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
    newDatabase.access_database()
    newDatabase.create_table(1)
    print(newDatabase.databases)
    print(newDatabase.tables)
