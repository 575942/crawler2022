import requests
import csv
import datetime
def spyder():
    videos = []
    # 保存
    class video:
        def __init__(self, title, director, rate):
            self.title = title
            self.director = director
            self.rate = rate
        def to_csv(self):
            return [self.title, self.director, self.rate]
        @staticmethod  # 静态
        def csv_title():
            return ["标题", "导演", "评分"]
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&year_range=2021,2021"
    r=requests.get(url=url,headers=head)
    r.encoding=r.apparent_encoding
    if r.status_code==200:      #判断网页是否请求成功
        #回字符串的json对象，还需要解析
        page_text = r.json()  # 返回序列化好的实例对象，此处是列表中嵌套字典的数据
        print(page_text)
        all=page_text['data']
        for i in range(len(all)):
            title=all[i]['title']
            director = "".join(all[i]["directors"])     #将，替换，并改为字符串类型
            rate=all[i]["rate"]
            v=video(title,director,rate)
            videos.append(v)
    else:
        pass
    print("爬取成功！！！'")
    #保存文件
    save_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")  # 获取爬取时间
    file = f"豆瓣_动态网页{save_time}.csv"
    with open(file, "w", newline="",encoding="utf-8-sig")as f:
        pen = csv.writer(f)
        pen.writerow(video.csv_title())
        for i in videos:
            pen.writerow(i.to_csv())
    print("保存成功！！！")

if __name__=="__main__":
    spyder()
