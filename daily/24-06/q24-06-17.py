import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(c):
            remain = c-i**2
            if remain*2 < c:
                break
            root = int(math.sqrt(remain))
            if root*root == remain:
                return True
        return False