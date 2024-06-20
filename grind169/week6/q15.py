class Solution:
    # O(n)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        mySum = 0
        minSum = 0
        ans = [0,k-1] # include
        for i in range(k):
            mySum += abs(arr[i]-x)
        minSum = mySum
        for startIndex in range(1,n):
            endIndex = startIndex+k-1
            if endIndex >= n:
                break
            
              
            mySum -= abs(arr[startIndex-1]-x)
            mySum += abs(arr[endIndex]-x)
            if minSum > mySum:
                ans = [startIndex,endIndex-1] 
                minSum = mySum
        return arr[ans[0]:ans[1]+1]


    # O(log(n)), Bsearch
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # Bsearch to find the first element greater than x
        left = 0
        right = n-1
        while left<right:
            mid = (left+right)//2
            if arr[mid]>=x:
                right = mid 
            else:
                left = mid+1
        p = right
        if right != 0 and x-arr[right-1]<=arr[right]-x:
            p = right-1
        # p is the first element ,now spread to left or right from p
        p1 = p-1
        p2 = p+1
        # right is the target
        while p2-p1-1 != k:
            if p1<0:
                p2 += 1
            elif p2 >= n:
                p1 -= 1
            else:
                if x-arr[p1] <= arr[p2]-x:
                    p1 -= 1
                else:
                    p2 += 1
        return arr[p1+1:p2]
            