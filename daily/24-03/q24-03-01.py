class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ans = ['0']*n
        oneCnt = 0
        for c in s:
            if c == '1':
                oneCnt += 1
        
        ans[-1] = '1'
        oneCnt -= 1
        
        index = 0
        while oneCnt > 0:
            ans[index] = '1'
            index += 1
            oneCnt -= 1
        
        return ''.join(ans)
        


