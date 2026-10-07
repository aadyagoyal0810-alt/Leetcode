class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        x=set(nums[0])
        for i in range(1,len(nums)):
            x&=set(nums[i])
        return sorted(x)
