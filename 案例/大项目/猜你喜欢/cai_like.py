from cv2 import add
from scipy import rand
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pandas as pd
import random
from  proxies  import get_ip

'''登入'''
def login(accout,password,wb):
    wb.find_element_by_id('fm-login-id').send_keys(accout)  #输入账号
    wb.find_element_by_id('fm-login-password').send_keys(password) #输入密码
    wb.find_element_by_class_name('fm-btn').click() #登入
    time.sleep(15)
    #wb.find_element_by_xpath('//*[@id="J_SiteNavHome"]/div/a').click()  #返回淘宝首页
    #time.sleep(4)

def isElementExist(wb,element):
	flag=True
	try:
		wb.find_element_by_xpath(element)
		return flag
	except:
		flag=False
		return flag

def get_information(wb):
    data = {"商品名称": [], "商品图片": [], "商品价格": [], "商品成交量": [], "商品生产地": [], "店铺名称": []}
    #查看商品详细信息
    com_list=wb.find_elements_by_xpath('//div[@class="tb-recommend-content clearfix"]/div[@class="tb-recommend-content-item"]')
    print(len(com_list))
    for item in com_list:
        #名称
        name=item.find_element_by_xpath('.//div[@class="title"]').text
        print(name)
        data["商品名称"].append(name)
        #图片
        pic=item.find_element_by_xpath('.//div[@class="img-wrapper"]/img').get_attribute('src')
        print(pic)
        data["商品图片"].append(pic)
        #价格
        price=item.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/a/div[3]/span').text
        print(price)
        data["商品价格"].append(price)

        item.click()    #查看详细信息
        wb.switch_to.window(wb.window_handles[1])  #跳转到新页面
        time.sleep(3)  #等待跳转

        '''判断是天猫还是淘宝'''
        if isElementExist(wb,'/html/body/div[3]/div/h1/span/a'):  #天猫
            print("天猫")
            #成交量
            sold_num=wb.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/ul/li[1]/div/span[2]').text
            print(sold_num)
            data["商品成交量"].append(sold_num)
            #生产地
            address=wb.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[3]/dl/dd/div/span[1]').text
            print(address)
            data["商品生产地"].append(address)
            #店铺名称
            shop_name=wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/a/strong').text
            print(shop_name)
            data["店铺名称"].append(shop_name) 

        if isElementExist(wb,'/html/body/div[5]/div/div/div[1]/a'):
            print("淘宝")
            #成交量
            sold_num=wb.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/ul/li[6]/div/div/a/strong').text
            print(sold_num)
            data["商品成交量"].append(sold_num)
            #生产地
            address=wb.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div/div[1]/span[1]/span[1]').text
            print(address)
            data["商品生产地"].append(address)
            #店铺名称
            shop_name=wb.find_element_by_xpath('/html/body/div[6]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/dl/dd/strong/a').text
            print(shop_name)
            data["店铺名称"].append(shop_name)
        else:
            pass
        #关闭页面
        wb.close()  #关闭当前页面
        wb.switch_to.window(wb.window_handles[0])  #返回原始页面
        time.sleep(3)
        print("下一个")

    print(data)

    return data

def save_data(data):
    df=pd.DataFrame(data)
    df.to_csv("taobao_aoteman.csv",encoding="utf-8-sig")

if __name__=="__main__":
    # 创建谷歌浏览器操作对象，打开淘宝主页
    path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # --------------->找到本地的浏览器驱动
    wb= webdriver.Chrome(path)
    wb.maximize_window()  #最大化
    # 跳过滑块验证
    script = '''
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    '''
    wb.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
    url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.0.0.5af911d9cbXuJA&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F"
    wb.get(url)
    wb.implicitly_wait(3)

    # 输入账号和密码
    accout =""  # ----------------------------------------------->你的账号
    password = ""   # ---------------------------------------------->你的密码
    #登入
    login(accout,password,wb)
    #获取信息
    data=get_information(wb)
    #保存文件
    save_data(data)
    #清楚缓存
    wb.quit()