class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=1
        for i in range(1,n+1):
            s*=i
        s=str(s)
        x=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='0'):
                x+=1
            else:
                break
        return x
