#_*_ coding:utf-8 _*_;
# Canvas 画布容器 其中可以放置图形 文字 组件或者帧
#语法：canvas=Canvas(master,option='valur,...)
#master 父窗口 option 画布属性


from tkinter import *;
root=Tk();
root.resizable(0,0);
root.geometry('500x300');
canvas=Canvas(root,width=200,height=100);   #设置画布大小
canvas.pack();    #设置布局管理器
#绘制  左上方坐标为 10 10   右下方坐标为 50 50的正方向
canvas.create_rectangle(10,10,50,50);  #法1
p1=30,30;
p2=50,50;
canvas.create_rectangle(p1,p2,fill='orange');  #法2  加颜色

#三角形
#poly_gon  给坐标连成线
p3=100,50;
p4=100,40;
canvas.create_polygon(p1,p2,p3,fill='yellow',outline='blue');
canvas.create_polygon(p1,p2,p3,p4,fill='green');
root.mainloop();