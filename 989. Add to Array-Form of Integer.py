class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s=''
        for i in num:
            s+=str(i)
        s=int(s)
        s+=k
        l=[]
        s=str(s)
        for j in s:
            l.append(int(j))
        return l
