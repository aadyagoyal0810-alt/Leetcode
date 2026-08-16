class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                l.append(nums[i])
        return list(set(l)) 
