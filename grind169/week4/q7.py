class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        index = 0
        value = 0
        isPositive = True
        # delete leading space
        while index < n and s[index] == ' ':
            index += 1
        # check + or -
        if index == n:
            return value
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            isPositive = False
            index += 1
        # convert number
        def isNumber(c):
            try:
                val = int(c)
                return val
            except:
                return -1
        
        while index < n:
            result = isNumber(s[index])
            if result == -1:
                break
            else:
                value = value*10+result
                index += 1
        # judge range
        if not isPositive:
            value = -value
        if value < -2**31:
            value = -2**31
        elif value > 2**31 - 1:
            value = 2**31 - 1
        
        return value
