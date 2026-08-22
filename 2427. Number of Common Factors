class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x=0
        l=[]
        l1=[]
        for i in range(1,a+1):
            if(a%i==0):
                l.append(i)
        for j in range(1,b+1):
            if(b%j==0):
                l1.append(j)
        for i in l:
            if(i in l1):
                x+=1
        return x
