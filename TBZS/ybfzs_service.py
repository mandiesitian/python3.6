#_*_ coding:utf-8 _*_;
'''
实现异步阻塞方式，可以使用Asyncore模块实现异步方式，它也是处于网络处理的模块。
常用的方法：
handle_read():当socket有可读的数据的时候执行这个方法，可读的数据判定条件就是看
                readable()方法返回是True还是False。
handle_write()：当socket有可写的数据的时候执行这个方法，可写的数据判定条件就是看
                writeable()方法返回是True还是False。
handle_expt():当socket通信中出现OOB异常的时候执行此方法。
handle_connect():当有客户端连接时执行次方法。
handle_close():当连接关闭的时候执行此方法。
handle_error():当通信过程中出现错误且没有在其他的地方进行处理的时候执行此方法。
handle_accept():当作为sever socket监听且没有客户端连接的时候，利用此方法进行处理
readable():缓冲区是否有可读数据
writeable()：缓冲区是否有可写数据

'''



