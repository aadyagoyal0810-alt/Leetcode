class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        s=''
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if(strs[0][i]==strs[-1][i]):
                s+=strs[0][i]
            else:
                break
        return s
