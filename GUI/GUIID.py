#_*_ coding:utf-8 _*_;
# 当画布以create_开头的方法绘制图形时，会返回一个ID 通过图形ID对指定图形
# 进行相关操作 每一个图形的ID都不同 此ID为int型
from tkinter import *;
import time;
root=Tk();
root.resizable(0,0);
root.geometry('500x400');
canves=Canvas(root,width=500,height=400,bg='grey',bd=0);
canves.pack();
p1=100,10;
p2=100,60;
p3=150,35;
r=canves.create_polygon(p1,p2,p3,fill='yellow',outline='blue');
# create_方法返回ID 赋值给r
def movetriangle(event):
    if event.keysym=='Up':        #通过ID 移动图形
        canves.move(r,0,-3);
    if event.keysym=='Down':
        canves.move(r,0,3);
    if event.keysym=='Left':
        canves.move(r,-3,0);
    if event.keysym == 'Right':
        canves.move(r,3, 0);

canves.bind_all('<KeyPress-Up>',movetriangle);
canves.bind_all('<KeyPress-Down>',movetriangle);
canves.bind_all('<KeyPress-Left>',movetriangle);
canves.bind_all('<KeyPress-Right>',movetriangle);

root.mainloop();