from psutil import process_iter
from pytest import yield_fixture
import scrapy
from kong_book.items import KongBookItem

class NewbookSpider(scrapy.Spider):
    name = 'newbook'
    allowed_domains = ['www.kongfz.com/1004']  #多条下载，要调整url，一般只写域名
    start_urls = ['https://www.kongfz.com/1004']

    base_url="https://www.kongfz.com/1004/?page="
    page=1

    def parse(self, response):
        #pipelines：用于下载数据 
        #items：定义数据结构（下载的数据都有什么）
        print("===========================")
        div_list=response.xpath('//*[@id="listBox"]/div')
        for div in div_list:
            src=div.xpath('.//div[1]/a/img/@src').extract_first()  #picture
            name=div.xpath('.//div[2]/div[1]/a/text()').extract_first() #name
            price=div.xpath('.//div[3]/div[1]/div[1]/a/span[2]/text()').extract_first()#price
            book=KongBookItem(src=src,name=name,price=price)
        
            #获取一个book，并且交给piplines
            yield book
        #翻页爬取
        if self.page<100:
            self.page=self.page+1
            url=self.base_url+str(self.page)
        
            #怎么去调用parse方法
            yield scrapy.Request(url=url,callback=self.parse)
    