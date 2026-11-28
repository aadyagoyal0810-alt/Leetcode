class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=''
        for i in s:
            if(i in a):
                return i
            else:
                a+=i
