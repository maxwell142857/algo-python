class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        start,end = 0,n-1
        while start < n and s[start] == 0:
            start += 1
        while end >=0 and s[end] == '1':
            end -= 1

        oneCnt = 0
        ans = 0
        for i in range(start,end+1):
            if s[i] == '1':
                oneCnt += 1
            else:
                if s[i-1] != '0':
                    ans += oneCnt
        return ans
        