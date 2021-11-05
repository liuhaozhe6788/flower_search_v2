from database import *

myPassword = 'lfd6788'
myDatabase_name = 'flower_data'
myTables_name = ['flower_imgs']
newDatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)

def loaddata(newDatabase):
    newDatabase.create_table(myTables_name[0])
    print(newDatabase.databases)
    print(newDatabase.tables)
    newVal = ('https://tse2-mm.cn.bing.net/th/id/OIP-C.jMRpEwQ70HOoN57XLEa72AHaFj?pid=ImgDet&rs=1', 0, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://www.starrosesandplants.com/wp-content/uploads/2021/01/Elle_006.jpg', 0, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://cdn.shopify.com/s/files/1/0250/2151/3807/products/783d07a90fbff613fc0a0d0506858ccd.jpg?v=1617282312', 0, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://m.media-amazon.com/images/I/61WBuAzMmZL._AC_SX425_.jpg', 1, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://c8.alamy.com/comp/MB2HAP/camelia-bush-as-garden-hedge-in-full-bloom-MB2HAP.jpg', 1, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://live.staticflickr.com/207/452222788_130055c581_b.jpg', 1, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://hosstools.com/wp-content/uploads/2020/10/black-oil-sunflower.jpg', 2, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://www.gannett-cdn.com/presto/2020/09/10/USAT/636a3c3d-3b95-4f84-b492-e01b4b0794b4-Sunflower1.jpg', 2, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://tse2-mm.cn.bing.net/th/id/OIP-C.LiNaWzmDLq1_oceDVDxuiAHaDx?pid=ImgDet&rs=1', 2, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://gilmour.com/wp-content/uploads/2019/05/Jasmine-Care.jpg', 3, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://cdn.britannica.com/56/197956-050-5062911A/Arabian-jasmine.jpg', 3, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://www.lgbotanicals.com/thumbnail.asp?file=assets/images/Jasmine-grand-hydrosol-736.jpg&maxx=600&maxy=0', 3, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://tse1-mm.cn.bing.net/th/id/R-C.03c36e56c20e098f212892921c7b5d41?rik=3QdC9O4Idj%2bzog&riu=http%3a%2f%2friverdalepress.com%2fuploads%2foriginal%2f1508965244_7eef.jpg&ehk=KipCS35GpuxVhza7A5SQLeraKGojSfavHvg%2f4PF9qOg%3d&risl=&pid=ImgRaw&r=0', 4, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://tse3-mm.cn.bing.net/th/id/OIP-C.2SC4pNsBuGpRIl8rLWoe_AHaFm?pid=ImgDet&rs=1', 4, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    newVal = ('https://www.farmyardnurseries.co.uk/shop/User/Products/LrgImg/chrysanthemum-emperor-of-china2.jpg', 4, '*')
    newDatabase.insert_img_info(myTables_name[0], newVal)
    print(newDatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
    # print(newDatabase.select_url(myTables_name[0], 1))
    newDatabase.close()
    return newDatabase

if __name__ == "__main__":
    loaddata(newDatabase)