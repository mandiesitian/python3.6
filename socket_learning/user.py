#_*_ coding:utf-8 _*_;
import socket;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#建立连接
s.connect(('127.0.0.1',10000));
#接收欢迎信息
print(s.recv(1024).decode('utf-8'));

# for data in ['Tom','Jcak','Mike']:
while True:
    data=input('请输入要发送的信息');
    if(data=='exit' or not data):
        s.send(bytes('exit', encoding='utf-8'));
        s.close();
    else:
        data = bytes(data, encoding='utf-8');
        # 发送数据
        s.send(data);
    databack=s.recv(1024);
    str_data=databack.decode();
    print(str_data);



# s.send(bytes('exit',encoding='utf-8'));
# s.close();



