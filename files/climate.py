# -*- coding:utf-8 -*-
from __future__ import print_function
def disp_area():
    i=0;
    for a in climate_data:
        print('{:>2}:{:<6}'.format(i,a[0]),end='');
        i=i+1;
        if (i%5==0):            #每5个显示一行
            print();

def disp_temp(data):
    print("显示城市：",data[0]);
    print("--------------------------------------");
    end=len(data);
    for i in range(1,end):
        print('{:>2}月的平均气温是：{:>.1f}度'.format(i,float(data[i])));
    print("--------------------------------------");

target_file='climate.txt';
with open(target_file,'r') as fp:
    raw_data=fp.readlines();

climate_data=[];
for item in raw_data:
    a=item.rstrip('\n');
    b=a.split(' ');
    climate_data.append(b);

while True:
    disp_area();
    print();
    area=int(input('请输入要查询的城市的序号:(按下-1结束)'));
    if area==-1:break;
    else:
        disp_temp(climate_data[area]);
    x=input('按下enter返回主页面')

