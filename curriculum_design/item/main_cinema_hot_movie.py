import ttkbootstrap as ttk
from ttkbootstrap.constants import *  #添加主题
from PIL import Image,ImageTk
import tkinter as tk
import random
import city
import douban_picture
import glob
import numpy as np
import douban_data
import os

pic_dir=os.listdir("pictures")
for item in pic_dir:
    os.remove(os.path.join("pictures",item))  #删除picture文件中的图片，更新图片
'''创建窗口'''
class desktop():
    def __init__(self,master):
        #创建窗口
        self.root=master
        self.root.title("影院热门")
        self.root.geometry("1200x700")  #设置窗口的大小
        # 显示标题
        self.root.title_var = tk.StringVar()
        self.root.title_var.set("影院热门")
        initface1(self.root)

'''显示信息'''
class initface1():
    def __init__(self,master):
        self.master = master
        initface1.show_ip(self.master)  #显示IP地址
        initface1.show_picture(self.master)  #

    #显示ip地址
    def show_ip(self):
        ip_var=tk.StringVar()  #设置变量
        ip_var.set(f"您当前ip归属地是{location}")
        tk.Label(self.master,textvariable=ip_var,
                anchor=NW,   #位置在最上面
                font=("微软雅黑", 10)  #设置字体和大小
                ).pack(fill=X)  #x方向的填充
    #显示图片和信息
    def  show_picture(self):
        global photos,ip_list
        ip=random.choice(ip_list)
        picture_url=douban_picture.picture(random.choice(ip),location)  #获取图片的url列表
        #保存图片
        for i in range(len(picture_url)):
            douban_picture.save_picture(ip,picture_url[i])
        #读取图片
        photos_dir= glob.glob("pictures//*.jpg")
        photos_dir=sorted(photos_dir,key=os.path.getmtime)  #根据图片存储时间排序
        photos=[ImageTk.PhotoImage(Image.open(item).resize((200,230)))  for item in photos_dir]
        #显示图片
        container=ttk.Frame(master=self.master, padding=2,bootstyle=SECONDARY)
        container.pack(anchor=tk.CENTER,fill=X)
        matrix= np.arange(0,10,1).reshape(2,-1)
        #显示信息（电影名称、时长、是否邮票、评分）
        data=douban_data.get_data(ip,location)
        try:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    index=matrix[i][j]
                    #container.rowconfigure(matrix[i][j], weight=1)
                    container.columnconfigure(matrix[i][j], weight=1)  #自适应改变大小,放大比例是1    ->>>>>>>
                    photo_labels = ttk.Button(container, image=photos[index],
                                            compound=TOP,    #设置文字在图片的方位
                                            text=f"{data.get('name')[index]}({data.get('score')[index]})\n({data.get('duration')[index]})\n{data.get('enough')[index]}",
                                            #font=('微软雅黑',10),  #设置字体
                                            bootstyle=(LIGHT)
                                            )
                    photo_labels.grid(row=i,column=j,padx=20,pady=15)  #图片间距
        except:
            pass


if __name__=="__main__":
    with open("proxies.txt","r") as f:
        ip_list=f.readlines()
    location=city.get_city()  #当前电脑的ip地址
    root = tk.Tk()
    desktop(root)
    root.mainloop()