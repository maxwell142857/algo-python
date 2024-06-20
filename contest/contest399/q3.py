class Solution:
    # O(n*m)
    # TLE
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        new1 = [num for num in nums1 if num%k==0]
        new1.sort()
        nums2.sort()
        l1 = len(new1)
        l2 = len(nums2)
        cnt  = 0 
        for i in range(l1):
            for j in range(l2):
                if k*nums2[j]>new1[i]:
                    break
                if new1[i]%(k*nums2[j])==0:
                    cnt += 1
        return cnt