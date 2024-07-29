class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def isPrime(val):
            if val == 1:
                return False
            
            r = 2
            while r*r<=val:
                if val%r == 0:
                    return False
                r += 1
            return True
        
        cnt = 0
        root = int(l**(1/2))
        if root*root<l:
            root += 1
        while root*root<=r:
            if isPrime(root):
                cnt += 1
            root += 1
        return r-l+1-cnt

        