import requests
from lxml import etree

#豆瓣数据
def get_data(ip,city):
    url=f"https://movie.douban.com/cinema/nowplaying/{city}"
    head = {
        'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response=requests.get(url=url,headers=head,proxies={"http":ip})
    if response.status_code==200:
        response.encoding="utf-8"  #网页编码
        tree=etree.HTML(response.text)  #构建树
        data_name=tree.xpath('//*[@id="nowplaying"]/div[2]/ul/li/@data-title')  #获取名称
        data_score=tree.xpath('//*[@id="nowplaying"]/div[2]/ul/li/@data-score') #评分
        for i in range(len(data_score)):
            if data_score[i]=="0":
                data_score[i]="暂无评分"
        data_duration=tree.xpath('//*[@id="nowplaying"]/div[2]/ul/li/@data-duration')  #时长
        data_enough=tree.xpath('//*[@id="nowplaying"]/div[2]/ul/li/@data-enough')  #本地电影院是否有票
        for i in range(len(data_enough)):
            if data_enough[i]=="True":
                data_enough[i]="在售"
            else:
                data_enough[i]="售罄"
        data_details_url=tree.xpath('/html/body/div[3]/div[1]/div/div[1]/div[3]/div[2]/ul/li/ul/li[1]/a/@href')  #------------------>电影详细信息的url
        dic={
            "name":data_name,
            "score":data_score,
            "duration":data_duration,
            "enough":data_enough,
            "detail_url":data_details_url,
        }
    return dic