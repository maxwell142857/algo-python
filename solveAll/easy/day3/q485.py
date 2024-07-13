class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 0
        return max(ans,cnt)