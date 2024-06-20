class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum2cnt = defaultdict(int)
        preSum2cnt[0] = 1
        preSum = 0
        ans = 0
        for num in nums:
            preSum += num
            ans += preSum2cnt[preSum-k]
            preSum2cnt[preSum] += 1
        return ans
