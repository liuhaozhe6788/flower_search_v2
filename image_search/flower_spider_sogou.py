from PIL import Image
import requests
import numpy as np
import urllib
import json
import os
import shutil  # 用来删除文件夹
import datetime

from flower_spider_bing import num_imgs, num_imgs_per_class, num_class
from database import flowers_demapper

def getSogouImag(path):
    # 判断文件夹是否存在，存在则删除
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)

    for i in range(0, num_class):
        path_i = path + '/' + flowers_demapper[i + 1]
        os.mkdir(path_i)
        url_i = f'https://pic.sogou.com/napi/pc/searchList?mode=1&start=1&xml_len=150&query={flowers_demapper[i + 1]}'
        imgs = requests.get(url_i)
        imgs_text = imgs.text
        imgs_json = json.loads(imgs_text)
        imgs_json = imgs_json['data']
        imgs_items = imgs_json['items']
        for j in range(0, 30):
            if len(os.listdir(path_i)) == 10:
                break
            try:
                img_url = imgs_items[j]['picUrl']
                print('*********' + str(j) + '.png********' + 'Downloading...')
                print('下载的url: ', img_url)
                img_path_j = path_i + '/flower_' + str(j) + '.jpg'
                urllib.request.urlretrieve(img_url, img_path_j)
                Image.open(img_path_j)
                # img.show()
            except:
                continue
    print('Download complete !')

if __name__ == "__main__":
    time_stamp = datetime.datetime.now()
    print('===start=== at:', time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

    getSogouImag('./static/img')

    time_stamp = datetime.datetime.now()
    print('===end=== at:', time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))