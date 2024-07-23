class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        ans = [[0]*rowCnt for _ in range(colCnt)]

        for r in range(rowCnt):
            for c in range(colCnt):
                ans[c][r] = matrix[r][c]
        return ans