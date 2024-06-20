class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum2cnt = defaultdict(int)
        preSum2cnt[0] = 1
        preSum = 0
        ans = 0
        for num in nums:
            preSum = (preSum+num%k+k)%k
            ans += preSum2cnt[preSum]
            preSum2cnt[preSum] += 1
        return ans