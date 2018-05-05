#_*_ coding:utf-8 _*_;
from tkinter import *;
import time;
root=Tk();
root.resizable(0,0);
root.geometry('200x100');
canves=Canvas(root,width=200,height=100,bg='grey',bd=0);
canves.pack();
p1=10,10;
p2=10,60;
p3=50,35;
r=canves.create_polygon(p1,p2,p3,fill='yellow',outline='blue');
#r  创建三角形实例
for i in range(0,25):
    canves.move(r,5,0);   #id 为 的人的实例 向右移动5个像素  向下移动0个像素
    root.update();        #重新绘制画布
    time.sleep(0.05);     #使程序睡眠0.05秒后 在执行
root.mainloop();