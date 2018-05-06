#_*_ coding:utf-8 _*_;
#弹球游戏
from tkinter import *;
import random;
import time;
root=Tk();
root.wm_attributes('-topmost',1);
#使画布置于所有窗口之前
root.resizable(0,0);
# root.geometry('500x400');
root.title('BallGame');
canvas=Canvas(root,width=500,height=400,bg='blue',bd=0,highlightthickness=0);
canvas.pack();
root.update();

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas;
        self.id=canvas.create_oval(10,10,25,25,fill=color);
        self.canvas.move(self.id,245,100);

        start=[-3,-2,-1,1,2,3];
        random.shuffle(start);   #将start列表随机排列  值仍在start中

        self.x=start[0];
        self.y=-3;
        # self.x=random.randint(1,4);
        # self.y=random.randint(1,100);
        self.canvas_height=self.canvas.winfo_height();
        #获取画布当前高度
        self.canvas_width = self.canvas.winfo_width();
        #获取画布当前宽度
    def draw(self):
        self.canvas.move(self.id,self.x,self.y);
        pos=self.canvas.coords(self.id);   #coords返回画布上画好的x，y坐标  列表  上下左右


        if(pos[1]<=0):
            self.y=3;
        if(pos[3]>=self.canvas_height):
            self.y=-3;
        if(pos[0]<=0):
            self.x=3;
        if(pos[2]>=self.canvas_width):
            self.x=-3;

ball=Ball(canvas,'red');

while 1:
    ball.draw();
    root.update();
    time.sleep(0.01);







# root.mainloop();
