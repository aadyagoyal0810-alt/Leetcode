class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=s.split()
        l=[]
        for i in x:
            l.append(i[::-1])
        a=''
        for i in l:
            a=a+i+' '
        return a.rstrip()
