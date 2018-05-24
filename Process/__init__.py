#_*_ coding:utf-8 _*_;
'''
进程是应用程序正在执行的实体，每个进程至少要一件事，在一个进程内部有多个线程（子任务）
协程又称为微线程，协程的特点是一个线程执行，具有极高的执行效率
进程有唯一的ID

word 进程 可以进行打字、拼写检查没、打印等多个线程

线程是CPU调度的最小单元，进程不能直接与CPU进行交互，必须通过线程才可以
一个进程至少有一个线程，进程会启动一个主线程，该线程与该进程的ID 相同

主线程可以创建子线程，子线程亦可以创建子线程

'''
#单线程
'''
单线程就是按照顺序执行程序的方式，只有当一个子任务完成以后才执行后面的任务

'''

from time import ctime,sleep;

def music():
    for i in range(2):
        print('I am listen music {}'.format(ctime()));
        sleep(1);


def word():
    for i in range(2):
        print('I an write word{}'.format(ctime()));
        sleep(1);



music();
word();

'''
使用for  循环2次  每次休眠1秒
顺序执行，先执行music（） 在执行word（）  线程的存在必须依赖于进程
此段代码为单进程单线程  

'''