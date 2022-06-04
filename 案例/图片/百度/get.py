import requests

#获取百度网页信息
def getinformation(url):
    url = "https://www.baidu.com/"
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    responses=requests.get(url,timeout=5,headers=head)
    print("响应状态为：",responses.status_code)   #打印状态码
    print("请求的网络地址为：",responses.url)     #打印请求url
    print("头部信息为：",responses.headers)       #打印头部信息
    print("cookie信息为：",responses.cookies)     #打印cookie信息
    responses.encoding=responses.apparent_encoding
    html_text=responses.text
    print(html_text)                            #打印网页源代码
    return html_text

#爬取百度首页logo
def save_picture():
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    url = "https://m.baidu.com/se/static/img/iphone/logo.png"
    responses=requests.get(url=url,headers=head)
    picture=responses.content  #获取二进制类型数据
    print(picture)             #打印二进制数据
    #保存图片
    with open("baidu_logo.png","wb") as f:
        f.write(picture)

if __name__=="__main__":
    #getinformation(url)
    save_picture()

