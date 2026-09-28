class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            x=0
            for j in nums:
                if(j<i):
                    x+=1
            l.append(x)
        return l
        
