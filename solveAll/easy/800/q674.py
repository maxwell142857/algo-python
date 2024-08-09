class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        ans = 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 1
        return max(ans,cnt)