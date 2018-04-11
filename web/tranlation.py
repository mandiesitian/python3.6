import urllib.request;
import urllib.parse;
import json;

# content=input('请输入要翻译的内容:');
content=input('请输入翻译文档：');
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule';
data={};

data['i']=content;
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['lient']='fanyideskweb'
data['salt']='1523459118010'
data['sign']='feadaa7e6b29946b2f585b3204f1feae'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'

data=urllib.parse.urlencode(data).encode('utf-8');
response=urllib.request.urlopen(url,data);

html=response.read().decode('utf-8');
# print(html);
target=json.loads(html);
print('翻译结果：{}'.format(target['translateResult'][0][0]['tgt']));
