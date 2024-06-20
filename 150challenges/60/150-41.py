class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sPieces = s.split()
        if len(pattern) != len(sPieces):
            return False
        a2b = {}
        b2a = {}
        for index in range(len(pattern)):
            s1 = pattern[index]
            s2 = sPieces[index]
            if s1 not in a2b and s2 not in b2a:
                a2b[s1] = s2
                b2a[s2] = s1
            elif s1 in a2b and s2 in b2a:
                if a2b[s1] != s2 or b2a[s2] != s1:
                    return False
            else:
                return False
        return True