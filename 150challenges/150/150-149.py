class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(2) for _ in range(k+1)] for _ in range(n)]
        # dp[i][j][k] i: after deal i-th day, j: completed transaction cnt,k: hold or not 

        # keep holding stock in i-th day
        # dp[i][j][1] = dp[i-1][j][1]

        # keep not holding stock in i-th day
        # dp[i][j][0] = dp[i-1][j][0]

        # buy the stock in i-th day
        # dp[i][j][1] = dp[i-1][j][0]-prices[i]

        # sell the stock in i-th day
        # dp[i][j][0] = dp[i-1][j-1][1]+prices[i]

        # initialize
        dp[0][0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0][1] = max(dp[i-1][0][1],-prices[i])
        for j in range(1,k+1):
            dp[0][j][1] = float('-inf')
        # dp
        
        for i in range(1,n):
            for j in range(1,k+1):
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j][0]-prices[i])
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j-1][1]+prices[i])
           
        ans  =  0
        for j in range(k+1):
            ans = max(ans,dp[n-1][j][0])
        return ans