class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n-1):
            curVal = int(s[i])
            nextVal = int(s[i+1])
            if curVal>nextVal and curVal%2==nextVal%2:
                return s[:i]+s[i+1]+s[i]+s[i+2:]
        return s