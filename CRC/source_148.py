#_*_ coding:utf-8 _*_;
import random;
import numpy as np;
import time;
def Source(n):

    data=np.random.randint(2,size=148*n);  #2: 0 1
    data=data.reshape(n,148);
    data_len=len(data);
    fp=open('source.txt','w');
    for i in range(0,data_len):
        temp_data=data[i];
        for j in range(0,len(temp_data)):
            temp_source=str(temp_data[j]);
            fp.writelines(temp_source+" ");
        fp.writelines("\n");

    fp.close();

start=time.clock();
Source(1000);
end=time.clock();

print(end-start);