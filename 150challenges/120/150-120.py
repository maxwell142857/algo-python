from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findK(start1,end1,start2,end2,k):
            if start1>end1:
                return nums2[start2+k]
            if start2>end2:
                return nums1[start1+k]
            l1 = end1-start1+1
            l2 = end2-start2+1
            index1 = start1+l1//2 # mid in right
            index2 = start2+l2//2 # mid in right
            m1 = nums1[index1] 
            m2 = nums2[index2]
            if m1>m2:
                if k > l1//2+l2//2:
                    return findK(start1,end1,index2+1,end2,k-(index2+1-start2))
                else:
                    return findK(start1,index1-1,start2,end2,k)
            else:
                if k > l1//2+l2//2:
                    return findK(index1+1,end1,start2,end2,k-(index1+1-start1))
                else:
                    return findK(start1,end1,start2,index2-1,k)
        
        totalLength = len(nums1)+len(nums2)
        if totalLength%2 == 0:
            number1 = findK(0,len(nums1)-1,0,len(nums2)-1,totalLength//2-1)
            number2 = findK(0,len(nums1)-1,0,len(nums2)-1,totalLength//2)
            return (number1+number2)/2
        else:
            return findK(0,len(nums1)-1,0,len(nums2)-1,totalLength//2)
                
s = Solution()
s.findMedianSortedArrays([1,3],[2,7])
