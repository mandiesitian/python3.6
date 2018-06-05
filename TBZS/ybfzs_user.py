#_*_ coding:utf-8 _*_;
'''
客户端使用asyncore模块编写异步代码
编写异步客户端主要是继承asyncore.dispatcher,覆盖它的几个方法，handle_read()
是读取服务器传回数据的方法，handle_write()是传数据给服务器的方法，writeable()
是判断是否执行handle_read()的依据。

'''
import asyncore,socket,time;
class HTTPClient(asyncore.dispatcher):
    def __init__(self,host,port):
        asyncore.dispatcher.__init__(self);
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM);
        self.connect((host,port));
        self.buffer='hellow world';
    def handle_connect(self):
        pass;
    def handle_close(self):
        self.close();

    def handle_read(self):
        strReceive=self.recv(1024);
        print('handle_read'+'Receive'+strReceive);

    def writable(self):
        return (len(self.buffer)>0);

    def handle_write(self):
        print('handle_write:'+self.buffer);
        sent=self.send(self.buffer);
        self.buffer=self.buffer[sent:];

client=HTTPClient('127.0.0.1',8888);
asyncore.loop();


