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
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas;
        self.id=canvas.create_oval(10,10,25,25,fill=color);
        self.canvas.move(self.id,245,100);
        self.paddle=paddle;

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

        self.hit_bottom=False;

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id);
        if(pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]):
            if(pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]):
                return True;
            else:
                return False;
        else:
            return False;


    def draw(self):
        self.canvas.move(self.id,self.x,self.y);
        pos=self.canvas.coords(self.id);   #coords返回画布上画好的x，y坐标  列表  左上右下


        if(self.hit_paddle(pos)==True):
            self.y=-3;
        else:
            if(pos[1]<=0):
                self.y=3;
            if(pos[3]>=self.canvas_height):
                self.y=-3;
            if(pos[0]<=0):
                self.x=3;
            if(pos[2]>=self.canvas_width):
                self.x=-3;


class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas;
        self.id=canvas.create_rectangle(0,0,150,10,fill=color);
        self.canvas.move(self.id,150,380);

        self.start=False;
        self.x=0;
        self.canvas_width=self.canvas.winfo_width();

        self.canvas.bind_all('<KeyPress-Left>',self.turn_left);
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right);
        self.canvas.bind_all('<KeyPress-Up>',self.game_start);
        self.canvas.bind_all('<KeyPress-Down>',self.game_stop);

    def turn_left(self,event):
        self.x=-4;

    def turn_right(self,event):
        self.x=4;
    def game_start(self,event):
        self.start=True;
    def game_stop(self,event):
        self.start=False;

    def draw(self):
        self.canvas.move(self.id,self.x,0);
        pos=self.canvas.coords(self.id);
        # print(pos);

        if(pos[0]<=0):
            self.x=0;
        if (pos[2] >= 500):
            self.x = 0;



paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red');
while 1:
    if(paddle.start==True):
        paddle.draw();
        ball.draw();
    root.update_idletasks();
    root.update();
    time.sleep(0.01);

# root.mainloop();








