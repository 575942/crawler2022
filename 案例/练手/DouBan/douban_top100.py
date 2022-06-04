import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time 

def get_information():
    global  videos
    try:
        #保存
        class  video:
            def __init__(self, name, num, qoute, show_time, director, actor):
                self.name=name
                self.num=num
                self.qoute=qoute
                self.show_time=show_time
                self.director=director
                self.actor=actor
            def to_csv(self):
                return [self.name,self.num,self.qoute,self.show_time,self.director,self.actor]
            @staticmethod  #静态
            def csv_title():
                return ["电影名称","排名","简介","上映时间","导演","主演"]
        for i in range(0,4):
            #指定url
            url = "https://movie.douban.com/top250?start="+str(i*25)
            #进行UA伪装
            head = {
                "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
            }
            #发送请求
            responses=requests.get(url=url,headers=head)
            htme_text=responses.text
            soup=BeautifulSoup(htme_text,"html.parser")  #解析器进行解析
            items=soup.findAll("div",{"class":"item"}) #查找所有内容
            #提取内容
            for itm in items:
                #电影名称
                name=itm.find("span",{"class":"title"}).text
                #电影排名
                num=itm.find("div",{"class":"pic"}).text
                #电影简介
                qoute=itm.find("span",{"class":"inq"}).text
                #上映时间
                show_time=itm.find("div",{"class":"bd"}).p.contents[2]   #内容的第三行
                show_time=show_time.replace("\n","")
                show_time=show_time.replace(" ","")
                show_time=show_time[:4]
                #导演
                Director = itm.find("div", {"class": "bd"}).p.contents[0]  #第一行内容
                Director=Director.replace("\n","")
                Director=Director.replace(" ", "")
                Director=Director[3:]
                Director = Director.split()  #用，隔开，形成列表
                director=Director[0].strip() #去除空格
                #主演
                Actor=Director[1]
                Actor=Actor[3:]
                Actor=Actor.replace("...","")
                Actor=Actor.split("/")
                actor=Actor[0]
                v=video(name,num,qoute,show_time,director,actor)  #v类等价于video
                videos.append(v)
        #csv保存信息
        save_time=datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")   #获取爬取时间
        filename=f"douban_TOP100 {save_time}.csv"
        with open(filename,"w",newline="",encoding="utf-8-sig") as f:
            pen=csv.writer(f)           #获取写入能力的笔
            pen.writerow(v.csv_title())     #读取写入的内容
            for v in videos:
                pen.writerow(v.to_csv())
    except:
        print("爬取异常！！！")
    
if __name__=="__main__":
    videos=[]
    #翻页抓取
    print("开始爬取...")
    get_information()
    time.sleep(1)
    print("爬取完成！！！")
