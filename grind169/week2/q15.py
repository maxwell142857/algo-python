class Solution:
    def reverseBits(self, n: int) -> int:
        bitCnt = 0
        copy = n
        while copy:
            copy >>= 1
            bitCnt += 1
        
        base = 2**31
        result = 0
        for _ in range(32):
            result += (n&1)*base
            base >>= 1
            n >>= 1
        return result