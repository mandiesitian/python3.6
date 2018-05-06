#_*_ coding:utf-8 _*_;
#弹球游戏
from tkinter import *;
import random;
root=Tk();
root.resizable(0,0);
root.geometry('500x400');
root.title('BallGame');
canvas=Canvas(root,width=500,height=400,bg='blue',bd=0);
canvas.pack();
root.update();

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas;
        self.id=canvas.create_oval(10,10,25,25,fill='color');
        self.canvas.move(self.id,245,100);

        start=[-3,-2,-1,1,2,3];
        random.shuffle(start);   #将start列表随机排列  值仍在start中

        self.x=start[0];
        self.y=-3;
        self.canvas_height=self.canvas.winfo_height();
        #获取画布当前高度
        self.canvas_width = self.canvas.winfo_width();
        #获取画布当前宽度





root.mainloop();
