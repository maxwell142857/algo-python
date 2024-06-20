class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        p1,p2 = 0,0
        while p1 < l1 and p2 < l2:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return l2-p2