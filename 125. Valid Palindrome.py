class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=''
        for i in s:
            if(i.isalnum()):
                x+=i
        a=x.lower()
        if(a==a[::-1]):
            return True
        else:
            return False
