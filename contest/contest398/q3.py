import math
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        digitCnt = 0
        sample = nums[0]
        while sample > 0:
            sample //= 10
            digitCnt += 1
        
        ans = 0 
        for _ in range(digitCnt):
            # for each position, count the digit 
            val2cnt = defaultdict(int)
            for i in range(n):
                val = nums[i]%10
                nums[i] //= 10
                val2cnt[val] += 1
            for val in range(10):
                ans += val2cnt[val]*(n-val2cnt[val])
        return ans//2