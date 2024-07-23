class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        ans = 0
        preIndex = -1
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                if preIndex == -1:
                    preIndex = i
                else:
                    ans = max(ans,i-preIndex)
                    preIndex = i
        return ans