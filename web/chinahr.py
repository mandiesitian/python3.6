# -*-coding:utf-8 -*-
from __future__ import print_function
from urllib.parse import urlparse;
url='http://www.chinahr.com/sou/?city=30%2C358%3B34%2C398&keyword=%E9%80%9A%E4%BF%A1%E5%B7%A5%E7%A8%8B%E5%B8%88&industrys=0&companyType=3&salary=0&degree=-1&refreshTime=-1&workAge=-1';

uc=urlparse(url);
print(uc);
print('nerloc:',uc.netloc);
print('path:',uc.path);

q_mads=uc.query.split('&');  #query :查询
print('query command:')
for i in q_mads:
    print(i,end=' ')
    print();