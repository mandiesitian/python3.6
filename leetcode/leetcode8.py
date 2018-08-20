#_*_ coding:utf-8 _*_;
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.lstrip(' ');
        list=[];
        for i in str:
            if(i=='-'):
                if len(list)==0:
                    list.append(i);
                else:break;

            elif i=='+':
                if len(list)==0:
                    list.append(i);
                else:break;
            elif i.isdigit():
                list.append(i);
            else:break;


        list_str = ''.join(list);
        if(len(list_str)==0):
            return 0;
        else:
            list_int=int(list_str);
            if   pow(-2,31)<=list_int<=pow(2,31)-1:
                return list_int;
            else:
                if list_int<0:
                    return pow(-2,31);
                else:return pow(2,31)-1;



        # if(len(list_int)==0):
        #    return 0;
        # else:return list_int;






str='    -123111sadjfbdjkfn'
a=Solution();
print((a.myAtoi(str)));
