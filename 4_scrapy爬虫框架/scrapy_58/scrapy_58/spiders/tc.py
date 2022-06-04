import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['wuhu.58.com/chuzu/?PGTID=0d300008-007f-dfff-0a46-96bdfecad56a&ClickID=2']
    start_urls = ['https://wuhu.58.com/chuzu/?PGTID=0d300008-007f-dfff-0a46-96bdfecad56a&ClickID=2']

    def parse(self, response):
        name_list=response.xpath("/html/body/div[6]/div[2]/ul/li/div[2]/h2/a/text()")  #后面加上text()：获取文本
        price_list=response.xpath("/html/body/div[6]/div[2]/ul/li/div[3]/div[2]/b/text()")
        print("=======================================================")
        #print(content.extract())
        for i in range(len(name_list)):
            #print(name)
            name=str(name_list.extract()[i]).strip()  #获取名称
            price=price_list.extract()[i]+"元/月" #获取价格
            print(name,price)
