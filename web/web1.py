import urllib.request;
response=urllib.request.urlopen('http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp');
html=response.read();
html=html.decode('utf-8');
print(html);