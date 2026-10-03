class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        s.sort()
        s.reverse()
        s.remove('1')
        s.append('1')
        return ''.join(s)  
