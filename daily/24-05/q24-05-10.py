class Solution:
    # O(n^2 log(n^2)),brute force
    # def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    #     n = len(arr)
    #     division = []
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             division.append((arr[i]/arr[j],arr[i],arr[j]))
    #     division.sort()
    #     return division[k-1][1:]
    

    # O(n*log(m^2)),where m is max(arr), binary search
    # def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    #     n = len(arr)
    #     # get the val, find the count of number <= val
    #     # return [cnt,numerator,denominator]
    #     # numberator/denominator is the maxVal of number
    #     # run in O(n)
    #     def getCnt(val):
    #         j = 1
    #         cnt = 0
    #         numerator,denominator = 0,1
    #         for i in range(n-1):
    #             while j<n and arr[i]/arr[j]>val:
    #                 j += 1

    #             if j == n:
    #                 break

    #             cnt += n-j
    #             if numerator/denominator < arr[i]/arr[j]:
    #                 numerator = arr[i]
    #                 denominator = arr[j]
    #         return [cnt,numerator,denominator]
        
    #     # run Bsearch 
    #     left = 0
    #     right = 1
    #     while left < right:
    #         mid = (left+right)/2
    #         result = getCnt(mid)
    #         if result[0] == k:
    #             return result[1:]
    #         elif result[0] < k:
    #             left = mid
    #         else:
    #             right = mid
    #     return []
                
    # treat this problem as merge n sorted list
    # 378:https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        