#_*_ coding:utf-8 _*_;
import numpy as np;

def Source_matlab(n):

    data=np.random.randint(2,size=148*n);  #2: 0 1
    data=data.reshape(n,148);
    data_len=len(data);
    fp=open('source_matlab.txt','w');
    for i in range(0,data_len):
        temp_data=data[i];
        for j in range(0,len(temp_data)):
            temp_source=str(temp_data[j]);
            fp.writelines(temp_source+" ");
        fp.writelines("\n");

    fp.close();

def Source1_fpga(n):
    data_source=np.random.randint(2,size=n*148);
    data_len=len(data_source);
    fp=open('source_fpga.txt','w');
    for i in range(0,data_len):
        temp=str(data_source[i]);
        fp.writelines(temp+"");

    fp.close();





Source_matlab(2);
Source1_fpga(2);