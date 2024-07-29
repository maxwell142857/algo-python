class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x,y):
            if y == 0:
                return x
            else:
                return gcd(y,x%y)
            
        val2cnt = Counter(deck)
        cnt = min(val2cnt.values())
        if cnt == 1:
            return False
        
        divisor = -1
        for v in val2cnt.values():
            if divisor == -1:
                divisor = v
            else:
                divisor = gcd(divisor,v)
        
        return divisor>1