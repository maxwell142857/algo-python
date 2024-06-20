class Solution:
    def minOperations(self, k: int) -> int:
        def check(cnt):
            if cnt%2:
                return (cnt//2+1)*(cnt//2+1+1)>= k
            else:
                return (cnt//2+1)**2 >= k
        
        left = 0
        right = 10**5

        while left < right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return right