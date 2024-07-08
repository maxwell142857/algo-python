class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        ans = nums[-1]-nums[0]
        for head in range(4):
            tail = 3-head

            ans = min(ans,nums[n-1-tail]-nums[head])
        return ans
                