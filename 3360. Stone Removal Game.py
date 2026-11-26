class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<10 or (n>=19 and n<27) or (n>=34 and n<40) or (n>=45 and n<49)):
            return False
        else:
            return True
