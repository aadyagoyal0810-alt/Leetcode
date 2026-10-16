class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x=[]
        y=[]
        l=[]
        for i in range(n):
            x.append(nums[i])
        for i in range(n,2*n):
            y.append(nums[i])
        for i in range(n):
            l.append(x[i])
            l.append(y[i])
        return l
