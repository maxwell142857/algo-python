class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c2cnt = {}
        for c in order:
            c2cnt[c] = 0
        ans = ''
        for c in s:
            if c in c2cnt:
                c2cnt[c] += 1
            else:
                ans += c
        for c in order:
            ans += c*c2cnt[c]
        return ans
