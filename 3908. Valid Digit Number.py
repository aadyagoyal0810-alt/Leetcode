class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n=str(n)
        x=str(x)
        if(x in n and n[0]!=x):
            return True
        else:
            return False
