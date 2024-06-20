class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        tmp = 0
        for num in nums:
            if tmp + num > 0:
                tmp += num
                ans = max(ans,tmp)
            else:
                tmp = 0
        return ans