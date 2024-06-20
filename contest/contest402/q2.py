class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        val2cnt = defaultdict(int)
        ans = 0
        for h in hours:
            ans += val2cnt[(24-h%24)%24]
            val2cnt[h%24] += 1
        return ans