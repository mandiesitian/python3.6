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
            if(list_str[0]=="+"):
                list_str.strip('+');
                a=1;
            if(list_str[0]=='-'):
                list_str.strip('-');
                a=-1;

            print(list_str)
            list_int=int(list_str);

            # if(a==1):
            #     if pow(-2,31)<=list_int<=pow(2,31)-1:
            #         return list_str;
            #     else:return pow(2,31)-1;
            # if(a==-1):
            #     if pow(-2, 31) <= -list_int <= pow(2, 31) - 1:
            #         return -list_str;
            #     else:return pow(-2,31);




str='    -12311111sadjfbdjkfn'
a=Solution();
print(type(a.myAtoi(str)));
