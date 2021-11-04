from database import *

myPassword = 'lfd6788'
myDatabase_name = 'flower_data'
myTables_name = ['flower_imgs']
newDatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)

def loaddata(newDatabase):
    newDatabase.create_table(myTables_name[0])
    print(newDatabase.databases)
    print(newDatabase.tables)
    newVal = ('https://www.680news.com/wp-content/blogs.dir/sites/2/2014/01/rose.jpg.jpg', 0, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://m.media-amazon.com/images/I/61WBuAzMmZL._AC_SX425_.jpg', 1, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg', 2, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://gilmour.com/wp-content/uploads/2019/05/Jasmine-Care.jpg', 3, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://www.photos-public-domain.com/wp-content/uploads/2011/03/magenta-hot-pink-chrysanthemums-close-up.jpg', 4, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    print(newDatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
    print(newDatabase.select_url(myTables_name[0], 1))
    newDatabase.close()
    return newDatabase

if __name__ == "__main__":
    loaddata(newDatabase)