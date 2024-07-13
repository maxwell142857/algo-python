class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1 = 0
        n1,n2 = len(g),len(s)
        for i in range(n2):
            if g[p1]<=s[i]:
                p1 += 1
                if p1 == n1:
                    return n1
        return p1