class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        # deal with thousand
        thousand = num//1000
        num = num%1000
        for i in range(thousand):
            ans += 'M'
        # deal with hundred
        hundred = num//100
        num = num%100
        if hundred == 4:
            ans += 'CD'
        elif hundred == 9:
            ans += 'CM'
        else:
            if hundred >= 5:
                hundred -= 5
                ans += 'D'
            for _ in range(hundred):
                ans += 'C'
        # deal with ten
        ten = num//10
        num = num%10
        if ten == 4:
            ans += 'XL'
        elif ten == 9:
            ans += 'XC'
        else:
            if ten >= 5:
                ten -= 5
                ans += 'L'
            for _ in range(ten):
                ans += 'X'
        # deal with one
        one = num
        if one == 4:
            ans += 'IV'
        elif one == 9:
            ans += 'IX'
        else:
            if one >= 5:
                one -= 5
                ans += 'V'
            for _ in range(one):
                ans += 'I'
        return ans
        