from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template

from database import *
from feature_extractor import FeatureExtractor

app = Flask(__name__)

n = 5

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

        # Save query img
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + \
                            datetime.now().isoformat().replace(":", ".") + "_" + file.filename  # create img path
        img.save(uploaded_img_path)  # save the image to the path

        # RUn search
        fe = FeatureExtractor()
        query = fe.extract(img=img)  # feature extract of uploaded img
        dists = np.linalg.norm(features_array - query, axis=1)  # calc L2 distance
        ids = np.argsort(dists)[0 : 2]  # sort dists return ids
        # print(ids)
        mydatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
        scores = [mydatabase.select_url(myTables_name[0], id + 1) for id in ids]
        mydatabase.close()
        # return dists ad img path
        # print(scores)

        return render_template("index.html", query_path=uploaded_img_path, scores=scores)
    else:
        return render_template("index.html")


if  __name__ == "__main__":
    app.run()
