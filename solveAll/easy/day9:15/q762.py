class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def checkBits(val):
            cnt = 0
            while val:
                cnt += val&1
                val >>= 1
            return isPrime(cnt)
        
        def isPrime(val):
            if val <= 1:
                return False
            base = 2
            while base*base <= val:
                if val%base == 0:
                    return False
                base += 1
            return True
        
        cnt = 0
        for val in range(left,right+1):
            if checkBits(val):
                cnt += 1
        return cnt