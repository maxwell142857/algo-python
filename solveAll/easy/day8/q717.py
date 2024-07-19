class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        p = 0
        while p < n-1:
            if bits[p] == 0:
                p += 1
            else:
                p += 2
        return p == n-1

