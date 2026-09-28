class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        for i in nums:
            if(i!=min(nums) and i!=max(nums)):
                flag=1
                return i
        if(flag==0):
            return -1
