from PIL import Image
import urllib.request
from pathlib import Path
import numpy as np
from database import *
from load_data import *

from feature_extractor import FeatureExtractor

def offline_FeatureExtractor():
    n = 5
    fe = FeatureExtractor()
    database = loaddata()
    print(database.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
    for i in range(n):
        # 从数据库取出图片的url
        img_url = database.select_url(myTables_name[0], i)
        urllib.request.urlretrieve(img_url, 'buffer.jpg')

        # 根据图片的url读取图片数据，提取图片的特征向量
        feature = fe.extract(img=Image.open('buffer.jpg'))
        print(feature)
        # print(type(feature), feature.shape)
        # feature_path = Path("./static/feature") / (img_path.stem + ".npy")
        # print(feature_path)

        # 保存特征向量到数据库
        # np.save(feature_path, feature)
    database.close()

if __name__ == "__main__":
    offline_FeatureExtractor()