class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=sorted(nums)
        b=a[::-1]
        if(nums==a or nums==b):
            return True
        else:
            return False
