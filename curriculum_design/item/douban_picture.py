import requests
from lxml import etree
import re

#电影封面二进制数据
def picture(ip,city):
    url=f"https://movie.douban.com/cinema/nowplaying/{city}"
    head = {
        'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response=requests.get(url=url,headers=head,proxies={"http":ip})
    if response.status_code==200:
        response.encoding="utf-8"  #网页编码
        tree=etree.HTML(response.text)  #构建树
        data_picture_url=tree.xpath('/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/ul/li/ul/li[1]/a/img/@src')  #图片
    return data_picture_url
#保存图片
def save_picture(ip,ph_url):
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    url=ph_url
    photo_id=re.findall(r"p\d+",url)[0]  #图片的id
    response=requests.get(url=url,headers=head,proxies={"http":ip})
    response.encoding="utf-8"
    picture=response.content  #获取二进制类型数据
    #保存图片
    with open(f"pictures/{photo_id}.jpg","wb") as f:
        f.write(picture)
