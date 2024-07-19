class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minA,minB = m,n
        for a,b in ops:
            minA = min(minA,a)
            minB = min(minB,b)

        return minA*minB