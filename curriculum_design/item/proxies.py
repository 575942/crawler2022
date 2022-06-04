import requests
from lxml import etree
import random

class get_ip:
    def __init__(self):
        self.proxies_link=[]
        self.lei1="ha"  #高匿代理
        self.lei2="tr"  #普通代理
    '''判断ip是否有效'''
    def check_proxy(ip):
        try:
            url="https://www.baidu.com"
            head = {
                'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
            }
            proxies={"http":ip}
            response=requests.get(url=url,headers=head,proxies=proxies,timeout=8)
            if response.status_code==200:
                #print(f"{ip}有效")
                with open("proxies.txt","a",encoding="utf-8",newline="") as f:  #保存有效的ip
                    f.write(ip+"\n")
                return True
        except Exception as e:
            print(f"{ip}无效")
            pass
    '''爬取ip'''
    def get_proxy(self,num_page):
        try:
            for page in range(num_page):
                print(f"正在爬取{page}页")
                url="https://www.kuaidaili.com/free/in"+str(self.lei1)+"/"+str(page+1)+"/"
                head = {
                    'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
                }
                response=requests.get(url=url,headers=head)
                if response.status_code==200:
                    response.encoding="utf-8"
                    tree = etree.HTML(response.text)
                    ip_list=tree.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
                    for i in ip_list:
                        if get_ip.check_proxy(i)==True:  #判断ip是否有效
                            self.proxies_link.append(i)
                    return self.proxies_link
        except Exception  as e:
            print(e)