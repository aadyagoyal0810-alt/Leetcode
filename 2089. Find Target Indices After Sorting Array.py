class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        if(target not in nums):
            return []
        else:
            l=[]
            for i in range(len(nums)):
                if(nums[i]==target):
                    l.append(i)
            return l
