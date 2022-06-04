import requests
import datetime

def spyder(usernames):
    head = {
        "User-Agent": "Mozilla/5.0 (LinuxAndroid 6.0Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36 Edg/90.0.818.62"
    }
    url = "http://dxx.ahyouth.org.cn/api/peopleRankStage?table_name=reason_stage145&level1=直属高校&level2=安徽工程大学&level3=计算机与信息学院团委&level4=数据科学202团支部"
    r = requests.get(url=url, headers=head)
    r.encoding = r.apparent_encoding
    if r.status_code == 200:
        page_text = r.json()  # 返回序列化好的实例对象，此处是列表中嵌套字典的数据
        a_ll = page_text["list"]["list"]
        for i in range(len(a_ll)):
            if a_ll[i]["username"]:
                username = a_ll[i]["username"]
                usernames.append(username)
    else:
        print("爬取失败")

    #保存文件
    #save_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")
    filename = "人员.txt"
    with open(filename, "w+",encoding="utf-8") as f:
        for name in usernames:
            name=name+"\n"
            f.write(name)

if __name__ == "__main__":
    usernames = []
    spyder(usernames)
    print(usernames)
