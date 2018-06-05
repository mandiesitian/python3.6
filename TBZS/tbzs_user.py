#_*_ coding:utf-8 _*_;
import socket;
def client():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);#TCP
    sock.connect(('127.0.0.1',8888));
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
同步阻塞方式，当执行函数recv(),send()时，如果没有数据需要处理，他们是处于
等待状态的，只有数据产生时，才会继续执行。
'''


