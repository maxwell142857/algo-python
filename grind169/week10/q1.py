class Solution:
    
    # merge,O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        def findK(k):
            p1,p2 = 0,0
            index = 0
            while p1<l1 and p2<l2:
                if index == k:
                    return min(nums1[p1],nums2[p2])

                if nums1[p1]<nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
                index += 1
            
            if p1 == l1:
                return nums2[k-l1]
            else:
                return nums1[k-l2]
        mid = (l1+l2)//2
        if (l1+l2)%2==0:
            return ((findK(mid-1)+findK(mid)))/2
        else:
            return findK(mid)

    # O(log(mn))
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     def findK(k,start1=0,end1=len(nums1)-1,start2=0,end2=len(nums2)-1):
    #         print(k,start1,end1,start2,end2)
    #         if start1>end1:
    #             return nums2[k-start1]
    #         if start2>end2:
    #             return nums1[k-start2]
            
    #         mid1 = (start1+end1)//2
    #         mid2 = (start2+end2)//2
    #         val1 = nums1[mid1]
    #         val2 = nums2[mid2]
    #         if k > mid1+mid2: # why like this,this equation split two mid into different part
    #             # k not in small half part
    #             if val1>val2:
    #                 start2 = mid2+1
    #             else:
    #                 start1 = mid1+1
    #         else:
    #             # k not in big half part
    #             if val1>val2:
    #                 end1 = mid1-1
    #             else:
    #                 end2 = mid2-1
    #         return findK(k,start1,end1,start2,end2)

    #     cnt = len(nums1)+len(nums2)
    #     if cnt%2==0:
    #         return (findK(cnt//2)+findK(cnt//2-1))/2
    #     else:
    #         return findK(cnt//2)


    # m = min(m,n) O(log(m))
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     # make nums1 the short one
    #     if len(nums1)>len(nums2):
    #         nums1,nums2 = nums2,nums1

    #     l1,l2 = len(nums1),len(nums2)
    #     n = l1+l2
    #     # x,x,x,end1,start1(index1),x,x,x,x
    #     # x,x,x,end2,start2(index2),x,x,x,x
    #     end1,end2 = float('-inf'),float('-inf')
    #     start1,start2 = float('inf'),float('inf')
    #     low = 0
    #     high = l1
    #     while low<=high:
    #         mid = (low+high)//2
    #         index1 = mid

    #         # both are ok, influence when n is odd
    #         # use n, answer in right part:min(start1,start2)
    #         # use n+1, answer in left part:max(end1,end2)
    #         # index2 = n//2-index1
    #         index2 = (n+1)//2-index1 

    #         start1 = nums1[index1] if index1!=l1 else float('inf')
    #         end1 = nums1[index1-1] if index1!=0 else float('-inf')
    #         start2 = nums2[index2] if index2!=l2 else float('inf')
    #         end2 = nums2[index2-1] if index2!=0 else float('-inf')
            
    #         if end1<=start2 and end2<=start1:
    #             # success
    #             if n%2==0:
    #                 return (max(end1,end2)+min(start1,start2))/2
    #             else:
    #                 # return min(start1,start2)
    #                 return max(end1,end2)
    #         elif end1>start2:
    #             high = mid-1
    #         elif start1<end2:
    #             low = mid+1
    #     return -1
            

 


    