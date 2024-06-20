class Solution:
    # O(n*m)
    # TLE
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9+7
        def calculate():
            if len(nums) == 1:
                return max(0,nums[0])
            dp = [0]*n
            dp[0] = max(0,nums[0])
            dp[1] = max(dp[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            return max(dp)
        ans = 0
        for index,val in queries:
            nums[index] = val
            ans = (ans+calculate())%MOD
        return ans

        

