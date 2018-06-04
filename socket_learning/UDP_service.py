#_*_ coding:utf-8 _*_;
'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接
发送数据包，但并不保证数的可靠性
'''
import threading;
import socket;
import time;

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);# socket.SOSK_DGRAM 表示UDP
#绑定端口
s.bind('127.0.0.1',10000);
print('监听端口.......');
while True:
    data,addr=s.recvfrom(1024);  #接收数据
    print('接收来自{}的信息'.format(addr));
    s.sendto('hellow ,{}'.format(addr));  #发送数据

