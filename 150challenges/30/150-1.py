from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1,index2,last = m-1, n-1, m+n-1
        while index1>=0 and index2 >= 0: 
                if nums1[index1] < nums2[index2]:
                        nums1[last] = nums2[index2]
                        index2 -= 1
                else:
                        nums1[last] = nums1[index1]
                        index1 -= 1
                last -= 1
        while index2>= 0:
                nums1[last] = nums2[index2]
                index2 -= 1
                last -= 1
merge([1,2,3,0,0,0],3,[2,5,6],3)