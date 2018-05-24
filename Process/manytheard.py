#_*_ coding:utf-8 _*_;
'''
Pyrhon  执行多线程的模块叫做threading
两个模块 thread 和 threading 来是实现多线程
threading提供了一个比thread模块更高层的API来提高线程的并发行，能够将
多个进程并发运行并共享内存

threading 常用方法
threading.Thread()  实例化对象，每个Thread对象对应一个线程，可以通过start()方法
                    运行线程
threading.activeCount()  返回当前’进程‘里面线程的个数  包含主线程
         .enumerate()  返回当前运行的Thread对象列表
         .setDaemon()  参数设置为True时，会将线程声明为守护线程 且必须
                        在start() 方法前面设置，不设置为守护线程 程序会被无限挂起
        .start() 启动线程
        .join([timeout])   主线程A中，创建了子线程B 并且在主线程A中使用了B.join()
                            那么，主线程A会在调用的地方等值，直到子线程B完成操作后，才接着往下执行，
                            那么在调用这个线程时可以使用被调用线程的join方法

                            参数表示超过这个时间，不管完没完都回收线程，然后主线程接着执行

'''

#听音乐的同时写文档
#此程序用python3.6 IDLE执行

from time import ctime,sleep;
import threading;
def music():
    for i in range(2):
        print('I am listen music {}'.format(ctime()));
        sleep(1);


def word():
    for i in range(2):
        print('I an write word{}'.format(ctime()));
        sleep(2);

threads=[];
t1=threading.Thread(target=music);       #定义多线程，执行music方法，只传方法名
threads.append(t1);
t2=threading.Thread(target=word);
threads.append(t2);

if __name__=='__main__':          #程序从此处开始执行
    for t in threads:
        t.setDaemon(True);      #将线程声明为守护线程，不声明线程会被无线挂起
        t.start();            #启动线程

    print('all over{}'.format(ctime()));


