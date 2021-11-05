from PIL import Image
import requests
from io import BytesIO
import numpy as np
from database import *

from feature_extractor import FeatureExtractor

n = 15
fe = FeatureExtractor()
mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
# print(mydatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
for i in range(n):
    # print(i)
    # 从数据库取出图片的url
    img_url = mydatabase.select_url(myTables_name[0], i + 1)
    # print(img_url)
    # 根据图片的url读取图片数据，提取图片的特征向量
    response = requests.get(img_url)
    feature = fe.extract(img=Image.open(BytesIO(response.content)))

    # 保存特征向量到数据库
    mydatabase.insert_np_array(myTables_name[0], feature, i + 1)
print(mydatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
mydatabase.close()
