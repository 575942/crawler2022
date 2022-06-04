from sys import path_importer_cache
import requests
from bs4 import BeautifulSoup
import csv

def get_information():
    videos=[]
    class video:
        def __init__(self,name,price):
            self.name=name
            self.price=price
        def to_csv(self):
            return [self.name,self.price]
        @staticmethod  # 静态
        def csv_title():
            return ["商品名称", "价格"]
    
    url = "https://www.amazon.cn/s?k=python&rh=p_72%3A2039715051&dc&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&qid=1622557390&rnid=664973051&ref=sr_nr_p_72_3"
    #UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    #发送请求
    responses = requests.get(url=url, headers=head)
    html_text = responses.text
    soup = BeautifulSoup(html_text, "lxml")  # 用解析器进行解析
    #提取列表
    items = soup.findAll("div", {
                          "class": "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"})
    #抓取目标
    for itm in items:
        price = itm.find("span", {"class": "a-offscreen"}).text
        name=itm.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
        v=video(name,price)
        videos.append(v)
    
    file_name = f"amazon_python.csv"
    with open(file_name, mode="w", newline="", encoding="utf-8-sig") as f:  # newline=""防止空行出现
        pen=csv.writer(f)
        pen.writerow(v.csv_title())
        for i in videos:
            pen.writerow(i.to_csv())

if __name__ == "__main__":
    get_information()  # 获取内容
