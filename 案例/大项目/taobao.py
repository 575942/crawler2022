from selenium import webdriver
import time
import pandas as pd

'''登入'''
def login(accout,password,wb):
    wb.find_element_by_id('fm-login-id').send_keys(accout)  #输入账号
    wb.implicitly_wait(4)
    wb.find_element_by_id('fm-login-password').send_keys(password) #输入密码
    wb.find_element_by_class_name('fm-btn').click() #登入

def get_information(wb):
    goods_key="奥特曼"   #---------------------------->改变搜索信息
    time.sleep(10) 
    wb.find_element_by_xpath('/html/body/header/article/nav/div/div/form/div[2]/div/div/div/div/input').send_keys(goods_key)
    wb.find_element_by_class_name('btn-search').click() 

    '''页面跳转问题'''
    time.sleep(1)
    #1.获取当前页面（跳转过来的页面）句柄：
    wb.window_handles[-1]
    #2.切换到新窗口：
    wb.switch_to.window(wb.window_handles[-1])  
    data={"商品名称":[],"商品图片":[],"商品价格":[],"商品成交量":[],"商品生产地":[],"店铺名称":[]}  
    for i in range(2):   #设置爬取的页数
        com_list=wb.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
        print(len(com_list))
        for item in com_list:
            #获取图片
            img=item.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
            data["商品图片"].append(img)
            #获取名称
            name=item.find_element_by_xpath('.//div[@class="row row-2 title"]').text
            data["商品名称"].append(name)
            #获取价格
            price=item.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price')
            data["商品价格"].append(price)
            #获取成交量
            sold_num=item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
            data["商品成交量"].append(sold_num)
            #获取生产地
            address=item.find_element_by_xpath('.//div[@class="location"]').text
            data["商品生产地"].append(address)
            #获取店铺名称
            shop_name=item.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
            data["店铺名称"].append(shop_name)
        #翻页
        wb.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[8]').click()
        print("翻页")
        time.sleep(3)
    return data

def save_data(wb):
    df=pd.DataFrame(get_information(wb))
    df.to_csv("taobao_aoteman.csv",encoding="utf-8-sig")

if __name__=="__main__":
    # 创建谷歌浏览器操作对象，打开淘宝主页
    path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"  # --------------->找到本地的浏览器驱动
    wb = webdriver.Chrome(path)
    # 跳过滑块验证
    script = '''
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    '''
    wb.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
    url = "https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.jianhua.0.0.5af911d9MUiZgk%26pm_id%3D1501036000a02c5c3739"
    wb.get(url)
    wb.implicitly_wait(3)

    # 输入账号和密码
    accout =""  # ----------------------------------------------->你的账号
    password = ""   # ---------------------------------------------->你的密码
    #登入
    login(accout,password,wb)
    #获取信息
    save_data(wb)