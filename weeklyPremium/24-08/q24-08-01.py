class Solution:
    # set, O(n^2)
    def longestRepeatingSubstring(self, s: str) -> int:
        used = set()
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                subS = s[i:j]
                if subS in used:
                    ans = max(ans,len(subS))
                else:
                    used.add(subS)
        return ans
    
    # dp, O(n^2)
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        # dp[i][j] means length of same substring end in i and j (exclusive)
        dp = [[0]*(n+1) for _ in range(n+1)]
        ans = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    continue
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans,dp[i][j])
        return ans
