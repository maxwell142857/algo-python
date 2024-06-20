class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9+7
        nums = [1]*n
        for _ in range(k):
            for i in range(1,n):
                nums[i] = (nums[i]+nums[i-1])%MOD
        return nums[n-1]