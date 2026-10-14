class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=0
        l=[]
        for i in nums:
            x+=i
            l.append(x)
        return l
