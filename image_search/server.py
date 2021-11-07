from PIL import Image
import os
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template

from flower_spider import num_imgs, num_imgs_per_class, num_class
from database import myPassword, myDatabase_name, myTables_name, Database
from feature_extractor import FeatureExtractor

app = Flask(__name__)

flowers_demapper = {
    1: '向日葵',
    2: '梅花',
    3: '牡丹',
    4: '兰花',
    5: '桂花',
    6: '水仙花',
    7: '玫瑰',
    8: '菊花',
    9: '凤仙花',
    10: '郁金香',
    11: '马蹄莲',
    12: '蝴蝶兰',
    13: '扶桑花',
    14: '山茶花',
    15: '栀子花',
    16: '杜鹃花',
    17: '灯笼花',
    18: '玉兰花',
}

# 从数据库读取所有的特征向量
mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
features = mydatabase.select_all_features(myTables_name[0])
mydatabase.close()
# print(features)

# 将所有特征向量转换为二维numpy序列
features_array = []
for i in range(num_imgs):  # i = 0 ~ n-1
    features_array.append(eval(features[i][0]))
features_array = np.array(features_array)
# print(features_array)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_img"]

        # 保存上传的图片
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + \
                            datetime.now().isoformat().replace(":", ".") + "_" + file.filename  # create img path
        img.save(uploaded_img_path)

        # 删除历史图片
        entries = os.listdir('./static/uploaded')
        if len(entries) > 10:
            os.remove(entries[0])

        # 运行搜索
        fe = FeatureExtractor()
        query = fe.extract(img=img)  # feature extract of uploaded img
        # dists = (features_array@query.T)/(np.linalg.norm(features_array, axis=1) * np.linalg.norm(features_array))
        dists = np.sum(np.abs(features_array - query), axis=1) # calc Manhattan distance
        # dists = np.linalg.norm(features_array - query, axis=1)  # calc L2 distance
        # print(len(dists))
        ids = np.argsort(dists)[0: 10]  # sort dists return ids
        # print(ids)

        # 统计每种花卉出现的频率
        freq = np.zeros(num_class)
        mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
        for _id in ids:
            for _i in range(num_class):
                if mydatabase.select_result(myTables_name[0], _id + 1) == i:
                    freq[_i] += 1
        # print(freq)

        # 将频率最高的花卉名称作为识别结果
        result_id = np.argmax(freq)
        result = flowers_demapper[np.argmax(freq)]
        # print(f"the flower is {result}")

        # 从数据库中读取URL，获得该种类花卉的图片
        mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
        # print(mydatabase.select_all_imgs_of_a_class(myTables_name[0], 1)[2][0])
        # scores = [mydatabase.select_url(myTables_name[0], id) for id in ids]
        scores = []
        for _i in range(min(num_imgs_per_class, 10)):
            scores.append(mydatabase.select_all_imgs_of_a_class(myTables_name[0], result_id)[_i][0])
        mydatabase.close()
        # print(scores)

        return render_template("index.html", query_path=uploaded_img_path, variable=result, scores=scores)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
