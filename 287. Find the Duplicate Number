class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=nums
        l.sort()
        for i in range(len(l)-1):
            if(l[i]==l[i+1]):
                return l[i]
