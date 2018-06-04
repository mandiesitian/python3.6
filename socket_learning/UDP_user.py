#_*_ coding:utf-8 _*_;
import socket;
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
# for data in ['Jack','Tome']:

data=input('请输入要发送的内容：');
s.sendto(bytes(data,encoding='utf-8'),('127.0.0.1',10000));
c=s.recvfrom(1024);
print(c);


