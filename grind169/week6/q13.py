class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        preSum = {}
        curSum = 0
        preSum[0] = -1
        maxL = 0
        for i in range(n):
            curSum += nums[i]
            if curSum not in preSum:
                preSum[curSum] = i
            else:
                maxL = max(maxL,i-preSum[curSum])
        return maxL
