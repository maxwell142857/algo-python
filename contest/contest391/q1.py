class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumOfDigit = 0
        copy = x
        while copy:
            sumOfDigit += copy%10
            copy //= 10

        if x%sumOfDigit == 0:
            return sumOfDigit
        else:
            return -1