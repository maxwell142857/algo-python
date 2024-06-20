class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # first calculate answer without ring
        ans = float("-inf")
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            ans = max(ans,preSum)
            preSum = max(preSum,0)
        
        # now find the minSubarray
        minAns = float("inf")
        minPreSum = 0
        for i in range(len(nums)):
            minPreSum += nums[i]
            minAns = min(minAns,minPreSum)
            minPreSum = min(minPreSum,0)

        if sum(nums) == minAns:
            return ans
        else:
            return max(sum(nums)-minAns,ans)