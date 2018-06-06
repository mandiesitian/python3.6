#_*_ coding:utf-8 _*_;
'''
读出
'''
import pprint,pickle;
pklfile=open('file.pkl','rb');
data1=pickle.load(pklfile);
print(data1);
data2=pickle.load(pklfile);
print(data2);

pklfile.close();
'''
这两个变量和原来的变量是完全不相干的两个对象，特们只是内容相容而已。
'''