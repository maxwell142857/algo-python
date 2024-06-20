class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        #  pre calculate and value from index i to j and store it into pre[i][j]
        pre = [[0]*n for _ in range(n)]
        for i in range(n):
            pre[i][i] = nums[0]
            for bias in range(n):
                if i+bias>=n:
                    break
                pre[i][i+bias] = pre[i][i+bias]&pre[i][i+bias-1]
        

        dp = [[-1]*m for _ in range(n)]

        if nums[0] == andValues[0]:
            dp[0][0] = nums[0]

        andVal = nums[0]
        for i in range(1,n):
            andVal &= nums[i]
            if andVal == andValues[0]:
                dp[i][0] = nums[i]
        
        for p2 in range(1,m):
            for p1 in range(n):
                result = float('inf')
                if p1 < p2:
                    continue
                andVal = nums[p1]
                if andVal == andValues[p2] and dp[p1-1][p2-1] != -1:
                    result = dp[p1-1][p2-1]+nums[p1]

                bias = 1
                while p1-bias-1>=0:
                    andVal &= nums[p1-bias]
                    if andVal == andValues[p2] and dp[p1-bias-1][p2-1] != -1:
                        result = min(result,dp[p1-bias-1][p2-1]+nums[p1])
                    bias += 1
                if result != float('inf'):
                    dp[p1][p2] = result
        
        return dp[n-1][m-1]
