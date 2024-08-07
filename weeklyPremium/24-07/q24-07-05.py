class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j] means the p when dealing i-th coins to reach j head on 
        dp = [[0]* (target+1) for _ in range(n)]
        dp[0][0] = 1-prob[0]
        if target >=1:
            dp[0][1] = prob[0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]*(1-prob[i])
        for i in range(1,n):
            for j in range(1,target+1):
                dp[i][j] = prob[i]*dp[i-1][j-1]+(1-prob[i])*dp[i-1][j]
        return dp[n-1][target]
