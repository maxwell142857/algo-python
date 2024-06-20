class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        # n >= 3
        ans = [0]*4
        ans[0] = nums[0]
        ans[1] = nums[1]
        ans[2] = nums[0]+nums[2]
        for i in range(3,n):
            ans[i%4] = max(ans[(i+2)%4],ans[(i+1)%4])+nums[i]
        
        return max(ans[(n-1)%4],ans[(n-2)%4])