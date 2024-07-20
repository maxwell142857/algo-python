class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        rowMin = [min(row) for row in matrix]
        colMax = []
        for c in range(colCnt):
            maxVal = matrix[0][c]
            for r in range(1,rowCnt):
                maxVal = max(maxVal,matrix[r][c])
            colMax.append(maxVal)
        
        ans = []
        for r in range(rowCnt):
            for c in range(colCnt):
                if matrix[r][c] == rowMin[r] and matrix[r][c] == colMax[c]:
                    ans.append(matrix[r][c])
        return ans