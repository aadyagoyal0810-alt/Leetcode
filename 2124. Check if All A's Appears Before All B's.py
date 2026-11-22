class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return list(s)==sorted(s)
