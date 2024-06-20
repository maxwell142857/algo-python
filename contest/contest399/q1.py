class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        cnt  = 0 
        for i in range(l1):
            for j in range(l2):
                if nums1[i]%(k*nums2[j])==0:
                    cnt += 1
        return cnt