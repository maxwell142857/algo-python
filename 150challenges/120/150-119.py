class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid-1
        if left == n-1:
            return nums[0]
        else:
            return nums[left+1]