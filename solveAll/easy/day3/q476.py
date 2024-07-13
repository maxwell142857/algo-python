class Solution:
    def findComplement(self, num: int) -> int:
        k = 0
        while 2**k-1<num:
            k += 1
        return 2**k-1-num