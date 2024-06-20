class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        cnt = 1
        p = 1
        ans = 1
        while p < n:
            if nums[p] == nums[p-1]+1:
                cnt += 1
                ans = max(ans,cnt)
                p += 1
            else:
                cnt = 1
                p += 1
        return ans

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for num in numSet:
            if num-1 in numSet:
                continue
            cur = num
            cnt = 1
            while cur+1 in numSet:
                cnt += 1
                cur += 1
            ans = max(ans,cnt)
        return ans