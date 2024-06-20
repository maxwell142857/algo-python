class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sSize = len(s)
        tSize = len(t)
        sIndex = 0
        tIndex = 0
        while tIndex< tSize and sIndex < sSize:
            if t[tIndex] == s[sIndex]:
                sIndex += 1
            tIndex += 1
        return sIndex == sSize
