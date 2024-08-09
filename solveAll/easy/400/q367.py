class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        base = 1
        while base*base<=num:
            if base*base == num:
                return True
            base += 1
        return False