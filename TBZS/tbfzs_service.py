#_*_ coding:utf-8 _*_;
'''
实现同步非阻塞方式，使用socket模块的sock.setblocking(0)方法，可以设置为非阻塞
方式。

'''
import time,socket;
def start():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);#TCP连接
    sock.bind(('127.0.0.1',8888));      #绑定sock
    sock.listen(1);
    print('正在监听端口...');
    clientsock,clientaddr=sock.accept();
    print('Connected by {}...'.format(clientaddr));
    while True:
        data=clientsock.recv(1024);
        if not data:
            break;

        time.sleep(2); #睡眠2秒


        clientsock.send(data);
        print('data={}'.format(data));

    clientsock.close();
    sock.close();

if __name__=='__main__':
    start();


