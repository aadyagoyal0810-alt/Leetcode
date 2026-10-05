class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        while(n!=1):
            if(n%2==0):
                n//=2
                x+=n
            else:
                n//=2
                x+=n
                n+=1
        return x
