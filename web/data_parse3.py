#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup;
import requests;

url='https://www.baidu.com';
html=requests.get(url).text;
sp=BeautifulSoup(html,'html.parser');

all_links=sp.find_all('a');
for link in all_links:
    herf=link.get('href');  #域名
    if(herf!=None and herf.startswith('http://') or herf.startswith('https://')):
        print(herf);