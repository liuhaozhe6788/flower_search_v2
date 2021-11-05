from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template

from database import *
from feature_extractor import FeatureExtractor

app = Flask(__name__)

n = 15
num_class = 5
m = int(n/num_class)
flowers_demapper = {
    0: '玫瑰',
    1: '山茶花',
    2: '向日葵',
    3: '茉莉',
    4: '菊花'
}

# 从数据库读取所有的特征向量
mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
features = mydatabase.select_all_features(myTables_name[0])
mydatabase.close()
# print(features)

# 将所有特征向量转换为二维numpy序列
features_array = []
for i in range(n):  # i = 0 ~ n-1
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
        img.save(uploaded_img_path)  # save the image to the path

        # 运行搜索
        fe = FeatureExtractor()
        query = fe.extract(img=img)  # feature extract of uploaded img
        dists = np.linalg.norm(features_array - query, axis=1)  # calc L2 distance
        # print(len(dists))
        ids = np.argsort(dists)[0 : m]  # sort dists return ids
        # print(ids)

        freq = np.zeros(num_class)
        mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
        for id in ids:
            for i in range(num_class):
                if mydatabase.select_result(myTables_name[0], id + 1) == i:
                    freq[i] += 1
        print(freq)
        result_id = np.argmax(freq)
        result = flowers_demapper[np.argmax(freq)]
        print(f"the flower is {result}")
        mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
        # print(mydatabase.select_all_imgs_of_a_class(myTables_name[0], 1)[2][0])
        scores = [mydatabase.select_all_imgs_of_a_class(myTables_name[0], result_id)[i][0] for i in range(min(m, 5))]
        mydatabase.close()
        # print(scores)

        return render_template("index.html", query_path=uploaded_img_path, variable=result, scores=scores)
    else:
        return render_template("index.html")


if  __name__ == "__main__":
    app.run()
