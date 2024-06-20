class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
    
    # space compress
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(2)]

        for i in range(2):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        for i in range(1,n):
            for j in range(1,m):
                dp[i%2][j] = dp[(i-1)%2][j]+dp[i%2][j-1]
        return dp[(n-1)%2][m-1]