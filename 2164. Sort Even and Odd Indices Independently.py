class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=[]
        y=[]
        l=[]
        for i in range(len(nums)):
            if(i%2==0):
                x.append(nums[i])
            else:
                y.append(nums[i])
        x.sort()
        y.sort()
        y.reverse()
        for i in range(len(x)):
            l.append(x[i])
            if(i<len(y)):
                l.append(y[i])
        return l
