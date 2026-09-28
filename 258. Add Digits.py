class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num<10):
            return num
        else:
            n=num
            x=0
            a=10
            while(a>9):
                a=0
                while(n>0):
                    x=n%10
                    a+=x
                    n//=10
                n=a
            return a
