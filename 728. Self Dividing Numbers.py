class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=[]
        if(left==0):
            for i in range(1,right+1):
                a=i
                h=0
                while(a>0):
                    x=a%10
                    if(x==0 or i%x!=0):
                        h=1
                        break
                    a//=10
                if(h==0):
                    l.append(i)
            return l
        else:
            for i in range(left,right+1):
                a=i
                h=0
                while(a>0):
                    x=a%10
                    if(x==0 or i%x!=0):
                        h=1
                        break
                    a//=10
                if(h==0):
                    l.append(i)
            return l
