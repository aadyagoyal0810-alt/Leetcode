class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        x=arr[0]-arr[1]
        flag=0
        for i in range(len(arr)-1):
            if(arr[i]-arr[i+1]!=x):
                flag=1
        if(flag==0):
            return True
        else:
            return False
