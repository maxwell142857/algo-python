class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        val2Index = {}
        preSum = 0
        val2Index[0] = -1
        n = len(nums)
        for i in range(n):
            preSum = (preSum+nums[i])%k
            if preSum in val2Index and i-val2Index[preSum]>=2:
                return True
            
            if preSum not in val2Index:
                val2Index[preSum] = i
        return False