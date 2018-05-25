#_*_ coding:utf-8 _*_;
'''
服务器端：监听服务的端口，等待客户连接
服务器地址、服务器端口号、客户端地址、客户端端口用来确定是哪一个socket
每一个连接都需要一个新的进程或者线程来处理，否则，服务器一次就只能服务一个客户端了

'''
import threading;
import socket;
import time;

def tcplink(sock,addr):
    print('接收新的连接。。。{}'.format(addr));

    sock.send('欢迎您！');
    while True:
        data=sock.recv(1024);   #接收客户端数据
        time.sleep(1);
        if data=='exit' or not data:  #数据是exit退出
            break;

        sock.send('您好，{}'.format(data));  #发送信息个客户端
    sock.close();             #关闭连接
    print('连接关闭{}'.format(addr));

#创建一个socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);  #socket.SOCK_STREAM表示TCP
s.bind(('127.0.0.1',10000));                 #监听本地10000端口
s.listen(5)                                 #最多5个连接

print('等待客户端连接....')

while True:
    # 接收一个连接
    sock,addr=s.accept();
    t=threading.Thread(target=tcplink,args=(sock,addr));
    #  创建线程来处理TCP连接

    t.start();

