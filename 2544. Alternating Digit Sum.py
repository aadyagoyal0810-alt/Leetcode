class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        n=str(n)
        for i in range(len(n)):
            if(i%2==0):
                x+=int(n[i])
            else:
                x-=int(n[i])
        return x
