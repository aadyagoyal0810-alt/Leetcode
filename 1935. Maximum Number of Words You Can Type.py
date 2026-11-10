class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        a=text.split()
        x=0
        for i in a:
            for j in brokenLetters:
                if(j in i):
                    break
            else:
                x+=1
        return x
