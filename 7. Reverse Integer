class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        if(x<0):
            a=int(math.fabs(x))
            z=0
            i=0
            l=a
            while(a>0):
                z=a%10
                i=i*10+z
                a//=10
            i=-i
        else:
            a=str(x)
            i=a[::-1]
            i=int(i)
        if(i>-2147483648 and i<2147483647):
            return i
        else:
            return 0
