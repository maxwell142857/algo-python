class Solution:
    # sliding windows, count when right pointer move 
    # O(n)
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     def LessOrEqual(t):
    #         left = 0
    #         cnt = 0
    #         ans = 0
    #         for right in range(n):
    #             if nums[right]%2:
    #                 cnt += 1
    #             while cnt > t:
    #                 if nums[left]%2:
    #                     cnt -= 1
    #                 left += 1
    #             ans += right-left
    #         return ans
    #     return LessOrEqual(k)-LessOrEqual(k-1)
    

    # preSum
    # O(n)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        pre2cnt = defaultdict(int)
        preSum = 0
        pre2cnt[0] = 1
        for num in nums:
            if num%2:
                preSum += 1
            ans += pre2cnt[preSum-k]
            pre2cnt[preSum] += 1
        return ans