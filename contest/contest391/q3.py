class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        left = 0
        for right in range(n):
            if left == right:
                cnt += 1
            else:
                if nums[right-1] == nums[right]:
                    left = right
                cnt += right-left+1
        return cnt