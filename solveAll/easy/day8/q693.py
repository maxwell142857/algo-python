class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n%2==0:
            m = n*2+1
        else:
            m = n*2
        result = m^n
        while result:
            if not result&1:
                return False
            result >>= 1
        return True