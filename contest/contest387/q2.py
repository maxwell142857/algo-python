class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        leftSum = [[0]*colCnt for _ in range(rowCnt)]
        for i in range(rowCnt):
            leftSum[i][0] = grid[i][0]
        
        for i in range(rowCnt):
            for j in range(1,colCnt):
                leftSum[i][j] = leftSum[i][j-1]+grid[i][j]
        
        ans = 0
        for j in range(colCnt):
            squareSum = 0
            for i in range(rowCnt):
                squareSum += leftSum[i][j]
                if squareSum <= k:
                    ans += 1
        return ans
