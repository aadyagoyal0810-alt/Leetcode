class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if(len(sentence)<26):
            return False
        else:
            l='qwertyuiopasdfghjklzxcvbnm'
            for i in l:
                if(i not in sentence):
                    return False
            return True
