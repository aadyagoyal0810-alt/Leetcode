class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        if(n==1):
            return [0]
        elif(n%2==0):
            for i in range(1,(n/2)+1):
                l.append(i)
                l.append(-i)
            return l
        else:
            l.append(0)
            for i in range(1,(n/2)+1):
                l.append(i)
                l.append(-i)
            return l    
