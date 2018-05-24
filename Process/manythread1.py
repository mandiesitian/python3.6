#_*_ coding:utf-8 _*_;
'''
加入jion（）函数，用于等待线程终止，在子线程完成运行之前，这个子线程的父线程将一直等待
'''

#用IDLE执行
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

if __name__=='__main__':
    for t in threads:
        t.setDaemon(True);
        t.start();
    t.join()
    print('all over {}'.format(ctime()));


'''
当程序执行时启动主线程，主线程又启动了一个听音乐的线程和一个写文档的线程，因为使用了join() 方法，只有当子线程运行结束
后，主线程才会继续执行在join()方法后面的代码，最后主线程推出，此乃单进程多线程

'''