class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 2**32
        
        val2val = '0123456789abcdef'
        ans = []
        while num > 0:
            ans.append(val2val[num%16])
            num //= 16
        ans = ans[::-1]
        return ''.join(ans)