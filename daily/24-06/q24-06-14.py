class Solution:
    # brute force
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                cnt += nums[i-1]+1-nums[i]
                nums[i] = nums[i-1]+1
        return cnt

