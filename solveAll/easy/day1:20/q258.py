class Solution:
    # O(n)
    def addDigits(self, num: int) -> int:
        def shrink(val):
            result = 0
            while val:
                result += val%10
                val //= 10
            return result
        
        while num >= 10:
            num = shrink(num)
        return num
    
    # O(1)
    # by math
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        else:
            return num%9