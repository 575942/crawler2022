import csv
import requests
from bs4 import BeautifulSoup
import time
import datetime

def get_information():
    try:
        n=int(input("请输入要爬取的页数:"))
        videos = []
        # 保存
        class video:
            def __init__(self,rooms, mianji, fangxiang,cengshu,nianfen,address):
                self.rooms = rooms
                self.mianji = mianji
                self.fangxiang = fangxiang
                self.cengshu=cengshu
                self.nainfen=nianfen
                self.address=address

            def to_csv(self):
                return [self.rooms, self.mianji, self.fangxiang,self.cengshu,self.nainfen,self.address]

            @staticmethod  # 静态
            def csv_title():
                return ["布局", "大小", "方向","楼层数","年份","地址","价格"]
        #UA伪装
        head = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }
        for i in range(n): 
            url = "https://fz.anjuke.com/sale/p"+str(i+1)+"/?from=esf_list"
            r = requests.get(url, headers=head)
            if r.status_code==200:
                r.encoding = r.apparent_encoding  # 编码
                time.sleep(1)
                soup = BeautifulSoup(r.text, "html.parser")
                items = soup.findAll("section", {"data": ""})
                for itm in items:
                    
                    if itm.find(
                        "p", {"class": "property-content-info-text property-content-info-attribute"})==None:
                        continue
                    else:
                        rooms =itm.find(
                                "p", {"class": "property-content-info-text property-content-info-attribute"}).text
                    mianji = itm.find_all("p")[1].text
                    fangxiang=itm.find_all("p")[2].text
                    cengshu=itm.find_all("p")[3].text
                    nianfen=itm.find_all("p")[4].text
                    address = itm.find(
                        "p", {"class": "property-content-info-comm-address"}).text
                    print(address)
                    #price=itm.find("")

                    v=video(rooms,mianji,fangxiang,cengshu,nianfen,address)
                    videos.append(v)  
            else:
                print("出错啦!")
        #保存文件
        save_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")
        file = f"D:\\python\\crawler\\my_crawler\\安居客\\安居客福州二手房价{save_time}.csv"
        with open(file, "w+",newline="", encoding="utf-8-sig")as f:
            pen = csv.writer(f)
            pen.writerow(video.csv_title())
            for i in videos:
                pen.writerow(i.to_csv())

        print("保存成功！！！")

    except Exception as e:
        print("异常:"+str(e))

if __name__ == "__main__":
    get_information()
