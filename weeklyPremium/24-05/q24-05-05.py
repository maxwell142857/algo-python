class Solution:
    # def kthLuckyNumber(self, k: int) -> str:
    #     digitCnt = 1
    #     while 2*(2**digitCnt-1) < k:
    #         digitCnt += 1
        
    #     def construct(cnt,order):
    #         result = []
    #         while order:
    #             result.append(order%2)
    #             order //= 2
    #         while len(result) != cnt:
    #             result.append(0)
    #         result = result[::-1]
    #         s = []
    #         for val in result:
    #             if val:
    #                 s.append(7)
    #             else:
    #                 s.append(4)
    #         return ''.join(str(c) for c in s)

    #     return construct(digitCnt,k-(2**digitCnt-1))
    
    # more elegant
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        mask = 1
        s = []
        while k:
            s.append(k%2)
            k //= 2
        s.pop() # delete leading 1
        s = s[::-1]
        ss = []
        for c in s:
            if c:
                ss.append('7')
            else:
                ss.append('4')
        return ''.join(ss)
