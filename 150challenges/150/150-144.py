class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        rowCnt = len(obstacleGrid)
        colCnt = len(obstacleGrid[0])
        dp = [[0]*colCnt for _ in range(2)]
        dp[0][0] = 1
        for i in range(1,colCnt):
            if not obstacleGrid[0][i]:
                dp[0][i] = dp[0][i-1]
        for i in range(1,rowCnt):
            if not obstacleGrid[i][0]:
                dp[i%2][0] = dp[(i-1)%2][0]
            else:
                dp[i%2][0] = 0

            for j in range(1,colCnt):
                if not obstacleGrid[i][j]:
                    dp[i%2][j] = dp[(i-1)%2][j]+dp[i%2][j-1]
                else:
                    dp[i%2][j] = 0
        return dp[(rowCnt-1)%2][colCnt-1]
