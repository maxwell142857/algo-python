class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = 0,n-1
        while left <  right:
            while left<right and nums[left]%2==0:
                left += 1
            while left<right and nums[right]%2==1:
                right -= 1
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
        return nums
