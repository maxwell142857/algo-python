class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        factorSum = 1
        base = 2
        while base*base<num:
            if num%base==0:
                factorSum += base
                factorSum += num//base
            base += 1

        if base*base == num:
            factorSum += base
        return factorSum==num
