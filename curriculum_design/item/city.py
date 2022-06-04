import requests
from lxml import etree

def get_city():
    print("正在获取IP地址...")
    url = "https://ip.900cha.com/"
    head = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response = requests.get(url=url, headers=head)
    if response.status_code == 200:
        response.encoding = "utf-8"  # 网页编码
        tree = etree.HTML(response.text)  # 构建树
        location = tree.xpath('/html/body/div/div/div/div[1]/div[1]/ul/li[4]/text()')
        location = location[0].strip()[-3:]  # 具体信息
    return location