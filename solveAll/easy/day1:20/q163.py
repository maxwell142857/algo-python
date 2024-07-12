class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        def isValid(a,b):
            return b>=a
        
        if not nums:
            return [[lower,upper]]
        ans = []
        if isValid(lower,nums[0]-1):
            ans.append([lower,nums[0]-1])

        for i in range(1,len(nums)):
            if isValid(nums[i-1]+1,nums[i]-1):
                ans.append([nums[i-1]+1,nums[i]-1])

        if isValid(nums[-1]+1,upper):
            ans.append([nums[-1]+1,upper])

        return ans