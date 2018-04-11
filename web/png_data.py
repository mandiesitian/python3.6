from bs4 import BeautifulSoup;
import requests;
from urllib.parse import urlparse;

url='http://www.ivsky.com/bizhi/lugu_lake_v46730/';
# a=urlparse(url);
# print(a);
domin='{}://{}'.format(urlparse(url).scheme,urlparse(url).hostname);
html=requests.get(url).text;
sp=BeautifulSoup(html,'html.parser');

all_links=sp.find_all(['a','img']);

for link in all_links:
    src=link.get('src');
    href=link.get('href');
    target=[src,href];
    for t in target:
        if t!=None and ('.jpg' in t or '.png' in t):
            if(t.startswith('http://')):
                print(t);
            else:
                print(domin+t);