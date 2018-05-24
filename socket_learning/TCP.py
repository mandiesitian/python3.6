#_*_ coding:utf-8 _*_;
'''
TCP
使用浏览器访问网页时使用TCP连接，浏览器实际上完成了socket网络通信，下面通过Python
实现TCP访问网页数据客户端的程序。
'''

import socket;
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#建立连接：指定服务器的IP地址和端口号，域名可以自动转换为IP地址
s.connect(('www.baidu.com',80));
s.send('GET/Http/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n');  #获取网页数据


buffer=[];
while True:
    d=s.recv(1024);

    if(d):
        buffer.append(d);
    else:
        break;

    data=''.join(buffer);

s.close();
header,html=data.split('\r\n\r\n',1);

print(header);
print(html);


