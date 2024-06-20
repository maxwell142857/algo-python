class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        hi = n-1
        # FFTTTTT
        while low < hi:
            mid = (low+hi)//2
            if nums[mid]>nums[0]:
                low = mid+1
            else:
                hi = mid
        if nums[hi]<nums[hi-1]:
            # there is a break point
            return nums[hi]
        else:
            # no rotate
            return nums[0]