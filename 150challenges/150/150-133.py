class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 5
        fiveCnt = 0
        tmpCnt = 0
        while number <= n:
            tmpCnt += 1
            fiveCnt += tmpCnt
            number *= 5
            
        return fiveCnt