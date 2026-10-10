class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if(-(nums[i]) in nums):
                return nums[i]
        return -1
