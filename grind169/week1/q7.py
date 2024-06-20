class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        sTimes = [0]*26
        tTimes = [0]*26
        for i in range(n):
            sTimes[ord(s[i])-ord('a')] += 1
            tTimes[ord(t[i])-ord('a')] += 1
        
        for i in range(26):
            if sTimes[i] != tTimes[i]:
                return False
        
        return True
