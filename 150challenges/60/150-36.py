class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for loop in range(n//2):
            for bias in range(n-2*loop-1):
                startR = loop
                startC = loop+bias
                tmp = matrix[startR][startC]
                matrix[startR][startC] = matrix[n-1-startC][startR]
                matrix[n-1-startC][startR] = matrix[n-1-startR][n-1-startC]
                matrix[n-1-startR][n-1-startC] = matrix[startC][n-1-startR]
                matrix[startR][n-1-startC] = tmp
        
                
