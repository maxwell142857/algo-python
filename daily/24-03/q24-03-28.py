class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        num2cnt = defaultdict(int)
        left = 0
        n = len(nums)
        ans = 0
        for right in range(n):
            number = nums[right]
            num2cnt[number] += 1
            while num2cnt[number]>k:
                num2cnt[nums[left]] -= 1
                left += 1
                
            ans = max(ans,right-left+1)
        return ans