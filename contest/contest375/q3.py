from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        n = len(nums)
        left = 0
        cnt = 0
        ans = 0
        for right in range(n):
            if nums[right] == target:
                cnt += 1
            if cnt == k:
                while nums[left] != target:
                    ans += n-right
                    left += 1
                ans += n-right
                left += 1 # now left point to the target's right
                cnt -= 1
        return ans
    

s = Solution()
s.countSubarrays([1,3,2,3,3],2)