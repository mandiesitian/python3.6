#_*_ coding:utf-8 _*_;
# 使用itemconfig（）方法可以改变画布上形状的某些属性
from tkinter import *;
root=Tk();
# root.resizable(0,0);
# root.geometry('500x300');
canvas=Canvas(root,width=200,height=150,bg='grey');
canvas.pack();

id1=canvas.create_polygon(10,10,10,60,50,35,fill='red');
id2=canvas.create_rectangle(10,60,70,120,fill='black');

def changecolor(event):
    if(event.keysym=='g' or event.keysym=='G'):
        canvas.itemconfig(id1,fill='green');
        canvas.itemconfig(id2, fill='green');
    if (event.keysym == 'b' or event.keysym == 'B'):
        canvas.itemconfig(id1, fill='blue');
        canvas.itemconfig(id2, fill='blue');

# canvas.bind_all('<KeyPress-g>,<KeyPress-G>',changecolor);  #' '中不可以有多个<>  只能分开写
# canvas.bind_all('<KeyPress-b>,<KeyPress-B>',changecolor);
canvas.bind_all('<KeyPress-b>',changecolor);
canvas.bind_all('<KeyPress-B>',changecolor);
canvas.bind_all('<KeyPress-G>',changecolor);
canvas.bind_all('<KeyPress-g>',changecolor);
root.mainloop();