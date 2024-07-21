class Solution:
    def minChanges(self, n: int, k: int) -> int:
        b1 = bin(n)[2:]
        b2 = bin(k)[2:]
        n1,n2 = len(b1),len(b2)
        if n1 < n2:
            return -1
        b2 = '0'*(n1-n2)+b2
        cnt = 0
        for i in range(n1):
            if b1[i] == b2[i]:
                continue
            elif b1[i] == '1' and b2[i] == '0':
                cnt += 1
            else:
                return -1
        return cnt