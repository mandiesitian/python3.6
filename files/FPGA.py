import math;

for i in range(0,192):
    j=2*math.floor(i/2)+(i+192-math.floor((16*i/192)))%2;
    print('{}:{}'.format(i,j));