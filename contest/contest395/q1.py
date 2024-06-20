class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = min(nums1)
        min2 = min(nums2)
        return min2-min1
