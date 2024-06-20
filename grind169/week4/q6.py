class Solution:
    # recursion with memo
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1:
            return False
        
        target = total//2
        nums.sort()
        memo = {}

        def construct(val,index):
            if val == 0:
                return True
            if val < 0:
                return False
            if index < 0:
                return False
            if (val,index) in memo:
                return memo[(val,index)]
            
            result = construct(val-nums[index],index-1) or construct(val,index-1)
            memo[(val,index)] = result

            return result
        
        return construct(target,len(nums)-1)
    
    # dp
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2==1:
            return False
        
        target = total//2
        dp = [[False]*(target+1) for _ in range(n)]

        if nums[0] <=target:
            dp[0][nums[0]] = True
        for i in range(1,n):
            dp[i][0] = True
        for i in range(1,n):
            for j in range(1,target+1):
                if nums[i]<=j:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] =  dp[i-1][j]
        return dp[n-1][target]
