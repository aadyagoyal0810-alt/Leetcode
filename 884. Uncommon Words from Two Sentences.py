class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        x=s1.split()
        y=s2.split()
        l=[]
        for i in x:
            if(i not in y and x.count(i)==1):
                l.append(i)
        for i in y:
            if(i not in x and y.count(i)==1):
                l.append(i)
        return l
