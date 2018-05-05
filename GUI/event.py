#_*_ coding:utf-8 _*_;
#在GUI程序中 每个组件都是一个对象 而组件使由属性、方法、事件组成的
#属性容纳程序要用到的数据 方法使执行的操作  事件是一种信息通知 所谓
#事件就是对象对外部动作的相应

#为对象建立一个处理某个事件的方法  这种方法称为绑定
#在python  中绑定分为三个级别  实例绑定 类绑定 和程序界面绑定

#（1）实例绑定是将事件与一个特定的组件实例绑定
# 组件实例.bind(事件描述符，事件处理方法）
# 例如  按下鼠标左键与canvas对象绑定画一条线
# canvas.bind('<Button-1>,drawline)
#（2）类绑定：将事件与一个组件类绑定
# 组件实例.bind_class(组件类，事件描述符，事件处理方法）
# 例如  绑定按钮类，所有按钮对象可处理鼠标左键操作事件
# widge,bind_class('Cancas','<Button_1>,drawline)
# (3) 程序姐年绑定：当界面中任何组件实例触发某个事件，程序都做出相应的处理
# 例如  将PrintScreen 键与程序中所有组件对象绑定
# widge.bind_all('<Key_Print>,printScreen')


# 事件队列 ： 包含一个或者多个事件类型的字符串
# 每个事件类型指定一项事件，当事件队列中有多项事件类型时，当且仅当描述符中
# 所有事件全部发生时才调用处理方法
# 事件类型定义如下：<[modifier] ...type[-detail]>
# modifier:用于组合键定义  如control  alt
# type：通用类型
# detail：明确定义是哪一个键或者按钮
# 如：<KeyPress-A>  表示按下键盘上A 键  <Button-1> 按下鼠标左键


# 事件类型：键盘事件 鼠标事件 窗体事件

# 键盘事件：KeyPress KeyRelease
# 鼠标事件：BuutonPress ButtonRelease ..
# 窗体事件: Map FocusIn(组件获得焦点时触发） FocusOut（推动焦点时触发）...





