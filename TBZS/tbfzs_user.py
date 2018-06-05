#_*_ coding:utf-8 _*_;
import socket;
def client():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);#TCP
    sock.connect(('127.0.0.1',8888));

    sock.setblocking(0);  #设置非阻塞方式


    while (1):
        print('请输入要发送的内容：');
        k=input();
        k=bytes(k,encoding='utf-8');
        sock.send(k);
        data=sock.recv(1024);
        print('Received{}'.format(data));
    sock.close();

if __name__=='__main__':
    client();


'''
因为再服务端接收数据后，等待2秒后才将数据返回给客户端，此时客户端设置的是非
阻塞方式，也就是再客户端执行函数recv()时，需要等待2秒才能得到服务端返回的数据，
非阻塞方式不允许由等待发生，所以会产生异常。

对比同步的阻塞和非阻塞方式，阻塞允许数据不立即返回，但它会一直处于等待接收数据的状态中，
不能执行其他的操作。
非阻塞方式不允许数据不立即返回，返回不及时，就会产生异常，可以捕获异常，再
进行其他的程序操作，也就是说程序不会一直是等待的状态，一旦出现异常，就可以去处理其他
的程序操作。


'''

