class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = float('inf')
        nums.sort()
        left = 0
        right =len(nums)-1
        while left < right:
            ans = min(ans,(nums[left]+nums[right])/2)
            left += 1
            right -= 1
        return ans