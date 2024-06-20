class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        maxValue = [float('-inf')]*colCnt
        for j in range(colCnt):
            for i in range(rowCnt):
                maxValue[j] = max(maxValue[j],matrix[i][j])
        
        ans = [[0]*colCnt for _ in range(rowCnt)]
        for i in range(rowCnt):
            for j in range(colCnt):
                if matrix[i][j] != -1:
                    ans[i][j] = matrix[i][j]
                else:
                    ans[i][j] = maxValue[j]
        return ans