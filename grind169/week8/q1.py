class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n  = -n
            x = 1/x
        ans = 1
        base = x
        while n:
            if n&1:
                ans *= base
            base *= base
            n >>= 1
        return ans
        