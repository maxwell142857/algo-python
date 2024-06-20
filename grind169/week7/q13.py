class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def cycleChange(i,j,l):
            lastVal = matrix[l-j][i]
            for _ in range(4):
                cur = matrix[i][j]
                matrix[i][j] = lastVal
                lastVal = cur
                i,j = j,l-i
        
        n = len(matrix)
        for level in range(n//2):
            length = n-level*2
            for bias in range(length-1):
                cycleChange(level,level+bias,n-1)
