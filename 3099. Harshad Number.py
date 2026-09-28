class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=x
        l=0
        i=0
        while(a>0):
            l=a%10
            i+=l
            a//=10
        if(x%i==0):
            return i
        else:
            return -1
