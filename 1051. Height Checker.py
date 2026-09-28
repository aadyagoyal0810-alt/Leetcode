class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        x=0
        z=sorted(heights)
        for i in range(len(heights)):
            if(heights[i]!=z[i]):
                x+=1
        return x
