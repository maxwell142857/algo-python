class Solution:
    def firstUniqChar(self, s: str) -> int:
        c2cnt = Counter(s)
        for i,c in enumerate(s):
            if c2cnt[c] == 1:
                return i
        return -1