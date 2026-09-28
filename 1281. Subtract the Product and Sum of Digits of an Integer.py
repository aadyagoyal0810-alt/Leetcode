class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=n
        x=0
        i=0
        p=1
        while(a>0):
            x=a%10
            i+=x
            p*=x
            a//=10
        return p-i
