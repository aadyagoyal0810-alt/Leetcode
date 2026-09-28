class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            if(i%6==0):
                l.append(i)
        if(len(l)==0):
            return 0
        else:
            return sum(l)/len(l)
