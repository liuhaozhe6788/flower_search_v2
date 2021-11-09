from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

from flower_spider_bing import num_imgs, num_imgs_per_class, num_class
from database import myPassword, myDatabase_name, myTables_name, Database, flowers_demapper
from server import features_array
from feature_extractor import FeatureExtractor

# 运行搜索
fe = FeatureExtractor()

m = 0
n = 0
num_list = np.zeros(num_class)
lens = 10
accu = np.zeros(lens)

for _iter in range(lens):
    for i in range(num_class):
        entries = os.listdir(f'./static/img/{flowers_demapper[i + 1]}')
        for j in entries:
            try:
                img = Image.open(f'./static/img/{flowers_demapper[i + 1]}/{j}')
            except:
                continue
            n += 1
            num_list[i] += 1
            # img.show()
            query = fe.extract(img=img)  # feature extract of uploaded img
            # dists = (features_array@query.T)/(np.linalg.norm(features_array, axis=1) * np.linalg.norm(features_array))
            dists = np.sum(np.abs(features_array - query), axis=1)  # calc Manhattan distance
            # dists = np.linalg.norm(features_array - query, axis=1)  # calc L2 distance
            # print(len(dists))
            ids = np.argsort(dists)[0: _iter + 15]  # sort dists return ids
            # print(ids)

            # 统计每种花卉出现的频率
            freq = np.zeros(num_class)
            mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
            for _id in ids:
                freq[int(mydatabase.select_result(myTables_name[0], _id + 1)) - 1] += 1
            # print(freq)

            # 将频率最高的花卉名称作为识别结果
            result_id = np.argmax(freq)
            if result_id == i:
                m += 1
    print(m)
    print(n)
    print(num_list)
    print(f"精确率为{m/n}%")
    accu[_iter] = m/n
    m = n = 0

x = np.arange(15, 25)
plt.xlabel("num of neighbors selected/*5")
plt.ylabel("accuracy")
plt.plot(x, accu)
plt.show()






