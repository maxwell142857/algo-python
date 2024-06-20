class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(base,exp):
            if exp < 0:
                base = 1/base
                exp = -exp
            
            result = 1
            tmpBase = base
            while exp:
                if exp & 1:
                    result *= tmpBase
                exp >>= 1
                tmpBase *= tmpBase
            return result
        
        return fastPow(x,n)