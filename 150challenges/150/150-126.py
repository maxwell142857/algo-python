class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        val = 0
        while n:
            ans.append(n%2)
            n //= 2
        remain0cnt = 32-len(ans)
        power = pow(2,remain0cnt)
        ans.reverse()
        for i in ans:
            val += i*power
            power *= 2
        return val