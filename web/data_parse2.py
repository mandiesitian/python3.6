from bs4 import BeautifulSoup;
import requests;
url='https://www.timeanddate.com/weather/';
html=requests.get(url).text;
# print(html);
sp=BeautifulSoup(html,'html.parser');
links=sp.find_all('img');
print(links[1]);