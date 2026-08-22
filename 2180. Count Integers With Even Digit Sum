class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        x=0
        for i in range(1,num+1):
            a=i
            s=0
            i=0
            while(a>0):
                i=a%10
                s+=i
                a//=10
            if(s%2==0):
                x+=1
        return x
