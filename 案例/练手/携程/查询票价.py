import csv
import requests
from bs4 import BeautifulSoup
import time
#json格式的列表叫数组 字典叫对象
def spyder():
    n = input("请输入你要订票的日期(2021-06-29):")
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62",
        "Cookie": "_uab_collina = 162410883290859257224879JSESSIONID = DF61F90D0BDB84FC1EE45E85F29C165Broute = c5c62a339e7744272a54643b3be5bf64BIGipServerotn = 770703882.64545.0000_jc_save_fromStation = %u5357 % u4EAC % 2CNJH_jc_save_toStation = %u971E % u6D66 % 2CXOS_jc_save_fromDate = 2021-06-19_jc_save_toDate = 2021-06-19_jc_save_wfdc_flag = dcRAIL_EXPIRATION = 1624450771215RAIL_DEVICEID = W3bgqLmESnf1c_fd4GCJ8H8BHWi6XgN9hWzEH9ajlr8yNjz9lAN6OhyhkbXzo8xk -dyL_LNZhYfZxj9Nbs_LY5PcC7DZ7QLq_cA5K1ogu9B5GSL_A78cF_fse_H -A7C6YGmveSSmCN3bFGSzvO5ch45NeLSiGBjV"
    }
    url = "https://trains.ctrip.com/trainBooking/search?ticketType=0&fromCn=%25E5%258D%2597%25E4%25BA%25AC%25E5%258D%2597&toCn=%25E9%259C%259E%25E6%25B5%25A6&day="+str(n)+"&mkt_header=&allianceID=&sid=&ouid=&orderSource=&trainsType=gaotie-dongche"
    r = requests.get(url=url, headers=head)
    videos = []
    # 保存
    class video:
        def __init__(self, checi, begin_time, end_time, sum_time, be_station, end_station, erzuowei,price,ticket):
            self.checi = checi
            self.begin_time = begin_time
            self.end_time = end_time
            self.sum_time = sum_time
            self.be_station = be_station
            self.end_station = end_station
            self.erzuowei = erzuowei
            self.price = price
            self.ticket=ticket
        def to_csv(self):
            return [self.checi, self.begin_time, self.end_time, self.sum_time, self.be_station, self.end_station, self.erzuowei,self.price,self.ticket]
        @staticmethod  # 静态
        def csv_title():
            return ["车次", "出发时间", "到站时间", "总时间", "始发站", "终点站","座位","票价","票数"]
    if r.status_code==200:
        time.sleep(1)
        #网页数据编码
        r.encoding=r.apparent_encoding
        #网页解析
        soup=BeautifulSoup(r.text,"html.parser")
        #网页总信息
        items = soup.findAll("div", {"class": "railway_list"})
        #获取各个信息
        for itm in items:
            checi = itm.find("strong").text
            begin_time = itm.find("div", {"class": "w2"}).find("strong").text
            end_time = itm.find("div", {"class": "w3"}).find("strong").text
            sum_time = itm.find("div", {"class": "haoshi"}).text
            be_station=itm.find("span").text
            end_station=itm.find("div", {"class": "w3"}).find("span").text
            erzuowei = itm.find("div", {"class": "w5"}).find("span").text
            price=itm.find("div", {"class": "w5"}).find("b").text
            ticket = itm.find("div", {"class": "w5"}).find(
                "strong", {"class": "TxtRed"}).text
            #数据分类
            v=video(checi,begin_time,end_time,sum_time,be_station,end_station,erzuowei,price,ticket)
            videos.append(v)

        #保存至文件
        file = f"D:\\python\\crawler\\my_crawler\\携程\\南京南至霞浦{n}.csv"
        with open(file, "w+", newline="", encoding="utf-8-sig")as f:
            pen = csv.writer(f)
            pen.writerow(video.csv_title())
            for i in videos:
                pen.writerow(i.to_csv())

        print("you are graet!")
    else:
         print("to go wrong!")

if __name__ == "__main__":
    spyder()

