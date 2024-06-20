class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1,2]
        for i in range(4,n+1):
            dp[i%4] = dp[(i+1)%4]+dp[(i+2)%4]+dp[(i+3)%4]
        return dp[n%4]