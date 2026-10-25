class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        x=''
        y=''
        for i in word1:
            x+=i
        for i in word2:
            y+=i
        if(x==y):
            return True
        return False
