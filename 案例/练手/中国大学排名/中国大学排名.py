"""
功能描述：
输入：大学排名的url链接
输出：大学排名信息的名目输出（排名、大学名称、总分）
"""
import requests
import csv
import datetime
import time

def gethtmltext():
    video=[]
    class videos:
        def __init__(self,college,rank,province):
            self.college=college
            self.rank=rank
            self.province=province
        def to_csv(self):
            return [self.college,self.rank,self.province]
        @staticmethod  #静态
        def csv_title():
            return ["名字","排名","省份"]
    #获取响应数据
    head={
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    url = "https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021"
    r=requests.get(url=url,headers=head,timeout=5)
    r.encoding = r.apparent_encoding  #解码
    if r.status_code==200:          #判断是否获取成功
        page_text=r.json()
        all=page_text["data"]["rankings"]
        for itm in all:
            college = itm["univNameCn"]
            rank = itm["rankOverall"]
            province = itm["province"]
            v=videos(college,rank,province)
            video.append(v)
    else:
        print("to go wrong！！！")

    #文本进度条
    scale = 10
    star = time.perf_counter()  # 计时
    print("saveing。。。".center(20, "="))
    #主循环
    for i in range(scale+1):  # range(11):0~10
        a = '*'*i
        b = '.'*(scale-i)
        c = (i/scale)*100
        dur = time.perf_counter()-star
        print("\r{:.2f}s[{}->{}]{:3.0f}%".format(dur, a, b, c), end="")
        time.sleep(0.2)  #调整进度的时间

    #保存文件
    save_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")
    filename=f"中国大学排名+{save_time}.csv"
    with open(f"D:\python\crawler\my_crawler\中国大学排名\{filename}",newline="",mode="w",encoding="utf-8-sig") as f:  #防止出现软吗
        pen=csv.writer(f)
        pen.writerow(videos.csv_title())  #写入标题
        for n in video:
            pen.writerow(n.to_csv())  #写入每一行信息
    print("\n"+"to save successfully！！！".center(20, "="))

if __name__=="__main__":
    gethtmltext()
