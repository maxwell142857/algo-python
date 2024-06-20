class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c2index = {}
        n = len(s)
        for i in range(n):
            c2index[s[i]] = i
        
        ans = 0
        for i in range(n):
            ans += abs(c2index[t[i]]-i)
        return ans