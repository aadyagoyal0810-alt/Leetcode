class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        a=len(matrix)
        b=len(matrix[0])
        x=[[0]*a for _ in range(b)] 
        for i in range(a):
            for j in range(b):
                x[j][i]=matrix[i][j]
        return x
