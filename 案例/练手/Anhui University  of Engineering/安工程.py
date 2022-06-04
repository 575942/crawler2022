import requests
from bs4 import BeautifulSoup
import time
def get_html_text(url):
    items_url=[]
    #进行UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    responses = requests.get(url=url, headers=head, timeout=5)
    responses.raise_for_status()  # 判断是否获取成功
    responses.encoding = responses.apparent_encoding  # 解码
    html_text = responses.text
    #打印前1000哥字符
    items_1000=html_text[:1000]
    print(items_1000)
    print("/n")
    soup=BeautifulSoup(html_text,"html.parser")
    #查找a标签的内容
    items_a=soup.findAll("a")  
    #抓取url
    for itm in items_a:
        item_url=itm.get("href")
        items_url.append(item_url)
    return items_a,items_url
def save_text():
    global  items_a,items_url
    filename="安徽工程大学主页a标签和url.txt"
    with open(filename,"w+",encoding="utf-8") as f:
        f.write(str(items_a))
        f.write(str(items_url))

if __name__ == "__main__":
    scale = 10
    star = time.perf_counter()  # 计时
    print("开始执行".center(20, "="))
    print("正在爬取...")
    url = "https://www.ahpu.edu.cn/"
    try:
        items_a,items_url= get_html_text(url)
    except Exception as e:
        print("异常："+str(e))
    try:    
        save_text()
    except Exception as e:
        print("异常："+str(e))
    #文本进度条
    for i in range(scale+1):  # range(11):0~10
        a = '*'*i
        b = '.'*(scale-i)
        c = (i/scale)*100
        dur = time.perf_counter()-star
        print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        time.sleep(0.2)
    print("\n爬取成功！！！")
    print("执行结束".center(20, "="))
