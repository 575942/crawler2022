import scrapy
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.ahpu.edu.cn']
    start_urls = ['http://www.ahpu.edu.cn/']

    def parse(self, response):
        print("*"*50)
        soup=BeautifulSoup(response.text,"html.parser")
        data=soup.select("li[class='news']")
        for item in data:
            print(item.text)