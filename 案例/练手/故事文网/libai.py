import requests
from bs4 import BeautifulSoup
import time

def get_html_text(url):
    global title,zuozhe_chaodai,shiju
    #保存
    class video:
        def __init__(self,title, zuozhe_chaodai, shiju):
            self.title = title
            self.zuozhe_chaodai = zuozhe_chaodai
            self.shiju = shiju
            
    #进行UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    responses = requests.get(url=url, headers=head, timeout=5)#
    responses.raise_for_status()  # 判断是否获取成功
    responses.encoding = responses.apparent_encoding  # 解码
    html_text = responses.text
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.findAll("div", {"class": "sons"})
    
    for itm in items:
        title.append(itm.find("p").find("a").find("b").text)
        zuozhe_chaodai.append(itm.find("p",{"class":"source"}).text)
        shiju.append(itm.find("div",{"class":"contson"}).text)
        
def save_text():
    global title, zuozhe_chaodai, shiju
    for i in range(len(title)):
        filename = "李白.txt"
        with open(filename, "a+", encoding="utf-8-sig") as f:
            f.write(str(title[i])+"\n")
            f.write(str(zuozhe_chaodai[i]))
            f.write(str(shiju[i])+"\n")
        
if __name__ == "__main__":
    title = []
    zuozhe_chaodai = []
    shiju = []
    url = "https://so.gushiwen.cn/shiwens/default.aspx?astr=%e6%9d%8e%e7%99%bd"
    try:
        print("正在爬取...")
        time.sleep(1)
        get_html_text(url)
    except:
        pass
    time.sleep(1)
    try:
        print("正在保存...")
        time.sleep(1)
        save_text()
        print("保存成功!!!")
    except Exception as e:
        print("异常："+str(e))
