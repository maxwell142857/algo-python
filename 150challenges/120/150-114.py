class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid
        
        if target < nums[0]:
            return 0
        else:
            return left+1