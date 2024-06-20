class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowCnt = len(grid)
        colCnt= len(grid[0])
        dp = [[0]*colCnt for _ in range(2)]
        dp[0][0] = grid[0][0]
        for i in range(1,colCnt):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1,rowCnt):
            dp[i%2][0] = dp[(i+1)%2][0]+grid[i][0]
            for j in range(1,colCnt):
                dp[i%2][j] = min(dp[(i+1)%2][j],dp[i%2][j-1])+grid[i][j]
        return dp[(rowCnt-1)%2][colCnt-1]