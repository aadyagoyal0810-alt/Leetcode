class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        x=0
        for i in range(len(nums)):
            if(nums[i]==1):
                x+=1
            else:
                l.append(x)
                x=0
        l.append(x)
        return max(l)
