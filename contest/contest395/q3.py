class Solution:

    # bit malipulation
    # We can split all bits of n - 1 and fill them into empty bits of x.
    # def minEnd(self, n: int, x: int) -> int:
    #     bX = bin(x)[2:]
    #     bX = list(bX[::-1])
    #     bN = bin(n-1)[2:]
    #     bN = list(bN[::-1])
    #     p1 = 0
    #     p2 = 0
    #     while p2 < len(bN):
    #         if p1 == len(bX):
    #             bX.extend(bN[p2:])
    #             break

    #         while p1<len(bX) and bX[p1] == '1':
    #             p1 += 1

    #         if p1 == len(bX):
    #             bX.extend(bN[p2:])
    #             break
    #         else:
    #             bX[p1] = bN[p2]
    #             p1 += 1
    #             p2 += 1
    #     return int(''.join(bX[::-1]),2)
    
    # bit malipulation, more elegant
    def minEnd(self, n: int, x: int) -> int:
        bitMask = 1
        n = n-1
        for _ in range(65):
            if x&bitMask == 0:
                # fill it with bit in n
                if n&1:
                    x = x|bitMask
                n >>= 1
                if n == 0:
                    break
            bitMask <<= 1
        return x
