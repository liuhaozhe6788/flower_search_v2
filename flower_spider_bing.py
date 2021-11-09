import requests
from bs4 import BeautifulSoup
import xlwt

from database import *

num_class = 18
num_imgs_per_class = 300
num_imgs = num_class * num_imgs_per_class

def web_scraping(class_num, imgs_num):
    """
    网络爬虫
    :params
    class_num:花卉种类个数
    imgs_num:每种花卉的图片个数
    :return
    """
    # 网络花卉图片爬虫
    url = 'http://cn.bing.com/images/async?q={0}&first={1}&count={2}&relp=35&lostate=r&mmasync=1&dgState=x*175_y*848_h*199_c*1_i*106_r*0'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}
    flowers_list = []
    with open('./static/txt/flowers_list.txt', 'r', encoding='utf-8') as file:
        for text in file.readlines():
            flowers_list.append(text[:-1].split(','))
    work_book = xlwt.Workbook()
    work_sheet = work_book.add_sheet('flowers_url')
    language = 1  #1按中文搜索，2按英文搜索
    batch_size = 150

    # 将图片信息存入一个excel表格和mySQL数据库中
    newDatabase = Database(mypassword=myPassword, database_name=myDatabase_name, tables_name=myTables_name)
    newDatabase.create_table(myTables_name[0])
    for i in range(class_num):
        print(i)
        for k in range(int(imgs_num/batch_size)):
            r = requests.get(url.format(flowers_list[i][language], k * batch_size, batch_size), headers=headers)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text)
                photo_list = soup.find_all('img', attrs={'class': 'mimg'})
                print(len(photo_list))
                for j in range(batch_size):
                    # 将图片的url（str）和种类结果（非负整数）存入excel表格中
                    work_sheet.write(i * imgs_num + k * batch_size + j, 0, str(i + 1))
                    work_sheet.write(i * imgs_num + k * batch_size + j, 1, photo_list[j]['src'])
                    work_sheet.write(i * imgs_num + k * batch_size + j, 2, flowers_list[i][0])
                    newVal = (photo_list[j]['src'], flowers_list[i][0], '*')
                    newDatabase.insert_img_info(myTables_name[0], newVal)
            else:
                print('获取该网页失败：' + flowers_list[i][0])
    print(newDatabase.data(myTables_name[0], ['img_id', 'img_url', 'flower_class', 'img_vector']))
    work_book.save('./data/flowers_url.xls')
    newDatabase.close()

if __name__ == "__main__":
    web_scraping(num_class, num_imgs_per_class)
