class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        l=[]
        for i in jewels:
            l.append(i)
        a=0
        for i in l:
            z=stones.count(i)
            a+=z
        return a
