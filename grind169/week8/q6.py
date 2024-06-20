class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x<0:
            isNegative = True
            x = -x
        digits = []
        while x > 0:
            digits.append(x%10)
            x //= 10
        if digits:
            val = int(''.join(str(digit) for digit in digits))
        else:
            val = 0
        if isNegative:
            val = -val
        if -2**31<=val<=2**31-1:
            return val
        else:
            return 0