class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        x=''
        for i in order:
            if(i in s):
                x+=i*s.count(i)
        for i in s:
            if(i not in order):
                x+=i
        return x
