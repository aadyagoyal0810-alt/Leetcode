class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<1 or len(nums)>1000):
            return False
        else:
            return nums*2  
