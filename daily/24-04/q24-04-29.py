class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        for num in nums:
            result ^= num
        delta = result^k
        cnt = 0
        while delta:
            if delta&1:
                cnt += 1
            delta >>= 1
        return cnt