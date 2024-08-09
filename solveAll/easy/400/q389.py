class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c2cnt = Counter(s)
        for c in t:
            if c2cnt[c] == 0:
                return c
            else:
                c2cnt[c] -= 1
        return '!'