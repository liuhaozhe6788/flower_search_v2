from database import *

myPassword = 'lfd6788'
myDatabase_name = 'flower_data'
myTables_name = ['flower_imgs']
myId = 0

def loaddata(myId=0):
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
    return newDatabase

if __name__ == "__main__":
    loaddata()