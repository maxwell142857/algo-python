class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        left = 0
        used = set()
        for right in range(n):
            c = s[right]
            while c in used:
                used.remove(s[left])
                left += 1
            used.add(c)
            cnt += right-left+1
        return cnt