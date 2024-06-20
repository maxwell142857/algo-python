class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        occupied = set()
        n = len(s)
        for i in range(n):
            cs = s[i]
            ct = t[i]
            if cs in s2t:
                if s2t[cs] != ct:
                    return False
            else:
                if ct not in occupied:
                    s2t[cs] = ct
                    occupied.add(ct)
                else:
                    return False
        return True