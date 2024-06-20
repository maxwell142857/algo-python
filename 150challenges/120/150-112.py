class Solution:
    # O(n^2)
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        for length in range(1,len(nums)+1):
            # initialization
            sum = 0
            for i in range(0,length):
                sum += nums[i]
            ans = max(ans,sum)
            # other situation
            end = length
            while end <len(nums):
                sum += nums[end]
                sum -= nums[end-length]
                ans = max(ans,sum)
                end += 1
        return ans
    
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            ans = max(ans,preSum)
            preSum = max(preSum,0)
            
        return ans