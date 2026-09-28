class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        for i in nums:
            a=i
            n=0
            i=0
            while(a>0):
                n=a%10
                i+=1
                a//=10
            if(i%2==0):
                x+=1
        return x
