class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        for i in range(len(nums)):
            x=0
            a=nums[i]
            j=0
            while(a>0):
                x=a%10
                j+=x
                a//=10
            if(j==i):
                flag=1
                return j
        if(flag==0):
            return -1
