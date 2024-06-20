class Solution:
    # sliding windows
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        minLength = 10 ** 6
        sum = 0
        for right in range(n):
            sum += nums[right]
            while sum >= target:
                minLength = min(minLength,right-left+1)
                sum -= nums[left]
                left += 1

        if minLength == 10**6:
            return 0
        else:
            return minLength
