class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=len(nums)-1
        while(i>=2):
            x=nums[i]
            y=nums[i-1]
            z=nums[i-2]
            if(y+z>x):
                return x+y+z
            i-=1
        return 0
