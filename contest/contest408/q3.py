class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for start in range(n):
            cnt0 = 0
            cnt1 = 0
            for end in range(start+1,n):
                if s[end] == '1':
                    cnt1 += 1
                else:
                    cnt0 += 1
                if cnt1>=cnt0*cnt0:
                    ans += 1
        return ans