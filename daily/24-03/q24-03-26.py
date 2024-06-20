class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        have = set(nums)
        ans = 1
        while True:
            if ans not in have:
                return ans
            else:
                ans += 1
    
    # cycle sort
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # use cycle sort
        p = 0
        while p < n:
            val = nums[p]
            if val < 0 or val > n:
                p += 1
            else:
                if nums[val-1] == val:
                    p += 1
                else:
                    nums[val-1],nums[p] = nums[p],nums[val-1]
        
        p = 0
        while p < n:
            if nums[p] != p+1:
                return p+1
            else:
                p += 1

        return n+1