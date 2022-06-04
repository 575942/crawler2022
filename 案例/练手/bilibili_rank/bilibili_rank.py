import  requests
from bs4 import BeautifulSoup
import csv
import datetime
import time

def get_information(url):
    print("正在获取内容...")
    try:
        #UA伪装
        head={
            "User-Agent":"Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
        }
        #发送请求
        responses=requests.get(url=url,headers=head)
        html_text=responses.text
        soup=BeautifulSoup(html_text,"html.parser")  #用解析器进行解析
        #提取列表
        items=soup.findAll("li",{"class":"rank-item"})
        time.sleep(2)  #休眠2秒
        print("成功提取内容！！！")
        return items
    except:
        time.sleep(2)  # 休眠2秒
        return "爬取失败"

def save_information():
    global items
    print("正在保存内容...")
    try:
        #保存信息
        vidoes=[]  #所有提取内容保存在vidoes列表中
        class vidoe:
            def __init__(self,title,rank,visit,up_name,score,up_id):
                self.title=title
                self.rank=rank
                self.visit=visit
                self.up_name=up_name
                self.score=score
                self.up_id=up_id
            def to_csv(self):
                return [self.title,self.rank,self.visit,self.up_name,self.score,self.up_id]  #生成一个列表
            @staticmethod   #是固定的，静态方法
            def csv_title():
                return ["标题","排名","播放量","up主","分数","id"]

        #抓取目标
        for itm in items:
            title=itm.find("a",{"class":"title"}).text  #抓取标题
            rank=itm.find("div",{"class":"num"}).text   #抓取排名
            visit=itm.find("span",{"class":"data-box"}).text  #抓取播放量
            up_name=itm.find("span",{"class":"up-name"}).text  #抓取up主名字
            score=itm.find("div",{"class":"pts"}).find("div").text  #抓取综合分数
            up_id = itm.find_all("a")[2].get("href")[len("//space.bilibili.com/"):]  # 抓取id(find_all所有a标签下的内容)
            #保存内容
            v = vidoe(title,rank,visit,up_name,score,up_id)
            vidoes.append(v)  #保存到列表
        print(len(vidoes))  #判断是否保存成功
        #用csv保存
        now_time=datetime.datetime.now().strftime("%Y年%m月%d日_%H时%M分%S秒")
        file_name = f"D:\\python\\crawler\\my_crawler\\bilibili_rank\\top100{now_time}.csv"
        with open(file_name,mode="w",newline="",encoding="utf-8-sig") as f:   #newline=""防止空行出现
            pen=csv.writer(f)  #比作一支笔
            pen.writerow(v.csv_title())  #写入首行
            for v in vidoes:
                pen.writerow(v.to_csv())
        time.sleep(1)
        print("保存成功！！！")
    except:
        return "保存失败"

if __name__=="__main__":
    #https://www.bilibili.com/v/popular/rank/life 生活区热门
    url = "https://www.bilibili.com/v/popular/rank/all"  #全站
    items=get_information(url)   #获取内容
    save_information()

