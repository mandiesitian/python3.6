from __future__ import print_function
import requests;
from bs4 import BeautifulSoup;
import urllib.request;

url='http://www.ivsky.com/bizhi/lugu_lake_v46730/';
html=requests.get(url).text;
# print(html);
sp=BeautifulSoup(html,'html.parser');

src_list=[];
all_link=sp.find_all('img');
for link in all_link:
    # print(link);
    src=link.get('src');
    src_list.append(src);
    # print(src);
for i in range(0,7):
    print(src_list[i]);

response=urllib.request.urlopen(src_list[0]);
lu_img=response.read();
with open('lugu_lake.jpg','wb') as fp:
    fp.write(lu_img);