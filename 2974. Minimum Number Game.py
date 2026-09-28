class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[]
        while(len(nums)!=0):
            x=min(nums)
            nums.remove(x)
            y=min(nums)
            nums.remove(y)
            arr.append(y)
            arr.append(x)
        return arr
