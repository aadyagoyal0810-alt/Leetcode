class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=s.split()
        z=''
        for i in range(k):
            z=z+a[i]+' '
        return z.strip()
