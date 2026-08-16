class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(len(nums)==1):
            return nums
        else:
            for i in nums:
                if(i==0):
                    nums.remove(0)
                    nums.append(0)
