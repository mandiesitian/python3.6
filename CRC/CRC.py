#_*_ coding:utf-8 _*_;

def sub_bit(N):
    dout=0;
    for i in range(0,N):
        dout=dout+pow(2,i);

    return dout;


def source(data):
    fp=open('CRC.txt','w');
    for i in range(0,data+1):
        dbin="{:0148b}".format(i);
        dbin=' '.join(dbin);
        print(dbin);
        fp.writelines(dbin+'\n');
    fp.close();

# source(7);

data_sum=sub_bit(148)
source(data_sum);
