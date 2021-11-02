import mysql.connector
from tabulate import tabulate

myPassword = 'lfd6788'
myDatabase_name = 'flower_data'
myTables_name = ['flower_imgs']
myId = 0

flowers_map = {
    'rose': 0,
    'camelia': 1,
    'sunflower': 2,
    'jasmine': 3,
    'chrysanthemum': 4
}

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
        self._mycursor = self._mydb.cursor(buffered=True)
        self._database_name = database_name
        self._mycursor.execute("show databases")
        self._databases_list = [x for x in self._mycursor]
        self._tables = tables_name
        self._tables_list_in_database = None
        print("class initialized")

    def close(self):
        self._mydb.close()

    # 创建表格
    def create_table(self, table_name: str):
        self._mycursor.execute(f"create table if not exists {table_name} (id int primary key, img_url varchar(255), \
                         result int unsigned, vector text) ")
        self._mycursor.execute("show tables")
        self._tables_list_in_database = [x for x in self._mycursor]

    # 插入一行信息
    def insert_img_info(self, table_name: str, val: tuple):
        sql = f"insert into {table_name} (id, img_url, result) values (%s, %s, %s)"
        self._mycursor.execute(sql, val)

    # 插入图片的特征向量
    def insert_np_array(self, ):
        pass

    # 选择图片的url信息
    def select_url(self, table_name: str, iter_id: int):
        self._mycursor.execute(f"select img_url from {table_name} where id = {str(iter_id)}")
        return self._mycursor.fetchone()[0]

    # 打印某张表的所有数据
    def data(self, table_name: str, table_headers: list):
        import copy
        self._mycursor.execute(f"select * from {table_name}")
        results = self._mycursor.fetchall()
        return copy.deepcopy(str(tabulate(results, headers=table_headers, tablefmt='psql')))

    # 获得所有数据库的名称
    @property
    def databases(self):
        import copy
        return copy.deepcopy(str(self._databases_list))

    # 获得本数据库flower_data的所有表格的名称
    @property
    def tables(self):
        import copy
        return copy.deepcopy(str(self._tables_list_in_database))


if __name__ == "__main__":
    newDatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
    newDatabase.create_table(myTables_name[0])
    print(newDatabase.databases)
    print(newDatabase.tables)
    newVal = (myId, 'https://www.680news.com/wp-content/blogs.dir/sites/2/2014/01/rose.jpg.jpg', 0)
    myId += 1
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = (myId, 'https://m.media-amazon.com/images/I/61WBuAzMmZL._AC_SX425_.jpg', 1)
    myId += 1
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = (myId, 'https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg', 2)
    myId += 1
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = (myId, 'https://gilmour.com/wp-content/uploads/2019/05/Jasmine-Care.jpg', 3)
    myId += 1
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = (myId, 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Chrysanthemum_November_2007_Osaka_Japan.jpg', 4)
    myId += 1
    newDatabase.insert_img_info(myTables_name[0], newVal)
    print(newDatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
    print(newDatabase.select_url(myTables_name[0], 0))
    newDatabase.close()

