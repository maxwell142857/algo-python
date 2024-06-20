class Solution:
    # brute force,O(n^2),TLE
    # def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
    #     n = len(nums1)
    #     cnt = 0
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if nums1[i]+nums1[j] > nums2[i]+nums2[j]:
    #                 cnt += 1
    #     return cnt
    
    # math,Bsearch,sort, O(n*lgn)
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        delta = [nums1[i]-nums2[i] for i in range(n)]
        delta.sort()
        cnt = 0
        for j in range(n):
            curVal = delta[j]
            # find all (i,j) for i<j
            left = 0
            right = j-1
            while left < right:
                mid = (left+right)//2
                if delta[mid]+curVal >0:
                    right = mid
                else:
                    left = mid+1
            if delta[left]+curVal>0:
                cnt += j-left
        return cnt
