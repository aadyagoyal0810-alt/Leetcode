class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if(n<=0):
            return False
        elif(n>0 and n<3):
            return True
        else:
            if(n%2!=0):
                return False
            else:
                while(n>1):
                    if(n%2!=0):
                        return False
                    n//=2
                return True
