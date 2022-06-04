import requests
from bs4 import BeautifulSoup
import time 

def get_html_text():
    keyword=input("请输入关键词:")
    url = "http://www.baidu.com/s?"
    keywd={
        "wd":keyword
    }
    #进行UA伪装
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    responses = requests.get(url=url,params=keywd,headers=head,timeout=5)
    responses.raise_for_status()  # 判断是否获取成功
    responses.encoding = responses.apparent_encoding  # 解码
    html_text = responses.text
    return html_text
def save_html():
    global html_text
    filename = "关键词.html"
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(html_text)
        
if __name__ == "__main__":
    try:
        html_text=get_html_text()
        print("爬取成功!!!")
    except Exception as e:
        print("异常："+str(e))
    time.sleep(1)
    try:
        save_html()
        print("保存成功!!!")
    except Exception as e:
        print("异常："+str(e))

