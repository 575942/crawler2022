# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from urllib import request
from itemadapter import ItemAdapter


class KongBookPipeline:
    def open_spider(self,spider):
        self.f=open("new_book.json","a",encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(str(item))
        return item
    
    def close_spider(self,spider):
        self.f.close()  #关闭文件
    

'''多条管道同时开启，保存图片'''
#(1)定义管道类
#(2)在settings中开启管道
#class KongBookdownload:
#    def process_item(self,item,spider):
#        url=item.get("src")  #获取url
#        filename=r"kong_book\spiders\book\\"+item.get("name")+".png"  #保存文件
#        request.urlretrieve(url=url,filename=filename)
#        return item
