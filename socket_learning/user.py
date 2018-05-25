#_*_ coding:utf-8 _*_;
import socket;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#建立连接
s.connect(('127.0.0.1',10000));
#接收欢迎信息
print(s.recv(1024).decode('utf-8'));

for data in ['Tom','Jcak','Mike']:
    s.send(data);
    print(s.recv(1024).decode('utf-8'));

s.send('exit');
s.close();



