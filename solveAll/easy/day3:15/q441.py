class Solution:
    def arrangeCoins(self, n: int) -> int:
        level = 0
        total = 0
        while True:
            if total+level+1>n:
                return level
            else:
                total += level+1
                level += 1

    # binary search
    def arrangeCoins(self, n: int) -> int:
        left,right = 0,n
        while left<right:
            mid = (left+right+1)//2
            if mid*(mid+1)//2 <= n:
                left = mid
            else:
                right = mid-1
        return left