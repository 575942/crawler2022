import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime

def get_information():
    container=[]
    class mafenwo:
        def __init__(self,address,name,comment,visit):
            self.address=address
            self.name=name
            self.comment=comment
            self.visit=visit

        def to_csv(self):
            return [self.address,self.name,self.comment,self.visit]
        #首行
        @staticmethod  # 是固定的，静态方法
        def csv_title():
            return ["景点", "地址", "蜂评", "游记"]
    #UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    n=input("请输入旅游地点：")
    url = "http://www.mafengwo.cn/search/q.php?q="+n+"&t=pois&seid=631D6DF2-FA6F-44DD-B51D-2EA9CCF3EE13"
    responses = requests.get(url,headers=head)
    try:
        if responses.status_code==200:
            print("状态码正常")
            time.sleep(1)
            responses.encoding = responses.apparent_encoding
            html_text=responses.content
            soup = BeautifulSoup(html_text, "html.parser")
            items=soup.findAll("li")
            for itm in items:
                #地址
                if itm.find("li")!=None:
                    address=itm.find("li").text
                    
                else:
                    continue
                #景点
                if itm.find("h3") != None:
                    n_ame = itm.find("h3").text
                    name = str(n_ame).replace("景点 - ", "")
                else:
                    continue
                #蜂评
                if itm.find_all("li")!=[]:
                    co_mment=itm.find_all("li")[1].text
                    c_omment=str(co_mment).replace("蜂评(","")
                    comment=str(c_omment).replace(")","")
                else:
                    continue
                #游记
                if itm.find_all("li") != []:
                    vi_sit = itm.find_all("li")[2].text
                    v_isit=str(vi_sit).replace("游记(","")
                    visit=str(v_isit).replace(")","")
                else:
                    continue
                m=mafenwo(address,name,comment,visit)
                container.append(m)
            print("爬取成功！！！")
    except Exception as e:
        print("异常"+str(e))
    try:
        print("正在保存...")
        time.sleep(1)
        #保存数据
        now_time = datetime.datetime.now().strftime("%Y年%m月%d日_%H时%M分%S秒")
        filename = f"马蜂窝_{n} {now_time}.csv"
        with open(filename, "w", newline="",encoding="utf-8-sig") as f:
            pen=csv.writer(f)
            pen.writerow(mafenwo.csv_title())  #写入首行标题
            for i in container:
                pen.writerow(i.to_csv())
        print("保存成功！！！")
    except Exception as e:
        print("异常"+str(e))

if __name__ == "__main__":
    get_information()  

