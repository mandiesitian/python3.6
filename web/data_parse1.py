# _*_ coding:utf-8 _*_
from __future__ import print_function;
import requests;
url='http://www.moe.gov.cn/jyb_xxgk/';  #中华人民共和国  公开网址

html=requests.get(url);
if(html.encoding!='utf-8'):
    html.encoding='utf-8';  #编码  使其显示中文
print(html.encoding);
html=html.text.splitlines();
for i in range(0,15):
    print(html[i]);