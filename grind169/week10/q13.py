class Solution:
    # use set
    def firstMissingPositive(self, nums: List[int]) -> int:
        have = set(nums)
        n = len(nums)
        for i in range(1,n+2):
            if i not in have:
                return i
        return -1
    
    # O(1) space 
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            val = nums[i]
            while 1<=val<=n and nums[val-1]!=val:
                tmp = nums[val-1]
                nums[val-1] = val
                val = tmp
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        