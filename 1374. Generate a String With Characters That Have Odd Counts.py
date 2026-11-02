class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n%2!=0):
            s='a'*n
        else:
            s='a'*(n-1)+'b'
        return s 
