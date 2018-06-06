#_*_ coding:utf-8 _*_;

'''
变量并不能保存到硬盘中，而需要一个序列化的过程，我们把变量从内存中变成可
存储或者传输的过程称之为序列化，在Python中称为pickling，序列化之后，就可以
将序列化后的内容写入硬盘或者通过网络传输到别的机器上。反之，把变量的内容从
序列化的对象重新读入内存中称之为反序列化，unpickling

Python提供两个模块实现序列化，cPickle和Pickle  先导入cPickle，如果失败，则导入
Pickle

try
    import cPickle as pickle
except ImportError
    import pickle
'''