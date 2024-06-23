class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [[0]*2 for _ in range(n)] # dp[i][0] means i-th num is -, dp[i][1] means i-th num is +
        dp[1][1] = nums[0]+nums[1]
        dp[1][0] = nums[0]-nums[1]
        for i in range(2,n):
            dp[i][0] = dp[i-1][1]-nums[i] # pre val must be +
            dp[i][1] = max(dp[i-1])+nums[i] # pre val can be + or -
        return max(dp[n-1])