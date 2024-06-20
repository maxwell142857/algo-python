class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        if 'CD' in s:
            ans += 400
            s = s.replace("CD","")
        if 'CM' in s:
            ans += 900
            s = s.replace("CM","")
        if 'XL' in s:
            ans += 40
            s = s.replace("XL","")
        if 'XC' in s:
            ans += 90
            s = s.replace("XC","")
        if 'IV' in s:
            ans += 4
            s = s.replace("IV","")
        if 'IX' in s:
            ans += 9
            s = s.replace("IX","")

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
        for char in s:
            if char == 'I':
                ans += 1
            elif char == 'V':
                ans += 5
            elif char == 'X':
                ans += 10
            elif char == 'L':
                ans += 50
            elif char == 'C':
                ans += 100
            elif char =='D':
                ans += 500
            elif char == 'M':
                ans += 1000
        return ans