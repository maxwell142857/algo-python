class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        if nums[1] < nums[0]:
            return 0
        if nums[n-2] < nums[n-1]:
            return n-1
        
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                right = mid
            else:
                right = mid
                
        return -1