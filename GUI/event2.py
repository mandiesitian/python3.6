#_*_ coding:utf-8 _*_;
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
canves.create_polygon(p1,p2,p3,fill='yellow',outline='blue');
def movetriangle(event):
    if event.keysym=='Up':
        canves.move(1,0,-3);
    if event.keysym=='Down':
        canves.move(1,0,3);
    if event.keysym=='Left':
        canves.move(1,-3,0);
    if event.keysym == 'Right':
        canves.move(1, 3, 0);

canves.bind_all('<KeyPress-Up>',movetriangle);
canves.bind_all('<KeyPress-Down>',movetriangle);
canves.bind_all('<KeyPress-Left>',movetriangle);
canves.bind_all('<KeyPress-Right>',movetriangle);

root.mainloop();




