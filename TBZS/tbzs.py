#_*_ coding:utf-8 _*_;
'''
实现同步阻塞方式，实际上使用socket模块就是同步方式，而且它默认时阻塞的。
服务端代码如下：
'''
import socket;
def start():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);#TCP连接
    sock.bind(('127.0.0.1',8888));      #绑定sock
    sock.listen(1);
    clientsock,clientaddr=sock.accept();
    print('Connected by {}...'.format(clientaddr));
    while True:
        data=clientsock.recv(1024);
        if not data:
            break;
        clientsock.send(data);
        print('data={}'.format(data));

    clientsock.close();
    sock.close();

if __name__=='__main__':
    start();
