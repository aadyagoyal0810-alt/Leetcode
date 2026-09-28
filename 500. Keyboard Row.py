class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        x=set('qwertyuiop')
        y=set('asdfghjkl')
        z=set('zxcvbnm')
        l=[]
        for i in words:
            a=set(i.lower())
            if(a<=x or a<=y or a<=z):
                l.append(i)
        return l
