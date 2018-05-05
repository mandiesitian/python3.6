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
canves.create_polygon(p1,p2,p3,fill='yellow',outline='blue');
#  创建三角形实例
def moverriangle(event):  #此方法参数列表可以是任何值  但不为空  一般为eent
    canves.move(1,5,0);

canves.bind_all('<KeyPress-A>',moverriangle);   #此方法无参数 只有方法名
root.mainloop();