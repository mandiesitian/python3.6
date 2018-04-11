import urllib.request;

response=urllib.request.urlopen('http://placekitten.com/500/600');
cat_img=response.read();

with open('cat_500_600.jpg','wb') as fp:
    fp.write(cat_img);   #二进制文件写入