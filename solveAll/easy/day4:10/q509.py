class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1,1]
        for i in range(3,n+1):
            dp[i%3] = dp[(i+2)%3]+dp[(i+1)%3]
        return dp[n%3]