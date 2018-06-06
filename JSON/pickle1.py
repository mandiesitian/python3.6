#_*_ coding:utf-8 _*_;
'''
尝试将对象序列化并写入文件
pickle.dump()
pickle.load()
pickle.dumps(obj):以字节对象返回封装的对象，不需要写入文件内
pickle.loads(bytes_obj)：从字节对象中读取被封装的对象。
'''
import pickle;
dicData={'data1':[2,8,4,3],
         'data2':('str1','str2'),
         'data3':None};
listData=[1,2,3];
output=open('file.pkl','wb');
pickle.dump(dicData,output);
pickle.dump(listData,output);
output.close();

'''
pickle.dump()直接把序列化后写入一个类文件对象，或者用pickle.dumps()把任意对象序列
会成一个str，然后将str写入文件。

'''