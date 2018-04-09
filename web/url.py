# -*- coding:urf-8 -*-
from urllib.parse import urlparse;
uc=urlparse('http://blog.sina.com.cn/s/blog_131651e210102y76l.html?tj=fina');
print(uc.netloc);         #parse  解析  urlparse 解析
print(uc.path);
print(uc.query);
print(uc);