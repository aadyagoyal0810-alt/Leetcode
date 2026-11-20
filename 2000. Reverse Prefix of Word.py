class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if(ch in word):
            s=''
            for i in word:
                if(i!=ch):
                    s+=i
                else:
                    break
            s+=ch
            s=s[::-1]
            a=s
            for i in range(word.index(ch)+1,len(word)):
                a+=word[i]
            return a
        else:
            return word
