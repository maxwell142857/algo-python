class Solution:
    def mySqrt(self, x: int) -> int:
        def check(root):
            return root*root <= x
        left = 0
        right = x
        while left < right:
            mid = (left+right+1)//2
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left
            