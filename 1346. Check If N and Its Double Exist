class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in arr:
            if(i==0):
                if(arr.count(0)>1):
                    return True
            elif(i*2 in arr):
                return True
        return False
