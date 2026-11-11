class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        x=0
        for i in words:
            for j in i:
                if(j not in allowed):
                    break
            else:
                x+=1
        return x
