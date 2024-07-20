class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxVal = nums[0]
        index = 0
        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                index = i
        for val in nums:
            if maxVal == val or val*2<=maxVal:
                continue
            else:
                return -1
        return index
        