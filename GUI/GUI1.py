#_*_ coding:utf-8 _*_
# 导入tkinter
# 创建GUI主窗口
# 添加各种组件
# 使用mainloop（）函数进入事件主循环  由用户触发第一个事件响应
#没有事件时 等待

#控制组件在界面中显示的位置需要布局管理器 pack（）方法就是将组件包装
#到一个父组件中 用于创建一个版面 还有grid（） place（）


import tkinter as tk;
root=tk.Tk();
root.title('top window');  #加入标题
root.resizable(1,1);
root.geometry('500x300');
tk.Button(root,text='save').pack();  #加入Button
tk.Button(root,text='cancle').pack();
root.mainloop();