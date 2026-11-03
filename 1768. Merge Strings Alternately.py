class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s=''
        if(len(word1)==len(word2)):
            for i in range(len(word1)):
                s+=word1[i]
                s+=word2[i]
        elif(len(word1)<=len(word2)):
            for i in range(len(word1)):
                s+=word1[i]
                s+=word2[i]
                a=i
            for j in range(a+1,len(word2)):
                s+=word2[j]
        else:
            for i in range(len(word2)):
                s+=word1[i]
                s+=word2[i]
                a=i
            for j in range(a+1,len(word1)):
                s+=word1[j]
        return s
