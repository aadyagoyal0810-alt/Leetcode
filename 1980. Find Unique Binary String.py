class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        import random
        s=nums[0]
        while(s in nums):
            s=''
            for i in range(len(nums)):
                s+=str(random.randint(0,1))
        return s
