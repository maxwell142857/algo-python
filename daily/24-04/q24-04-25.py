class Solution:
    # dp, O(n^2)
    # def longestIdealString(self, s: str, k: int) -> int:
    #     def isLegal(a,b):
    #         return abs(ord(a)-ord(b)) <= k
        
    #     n = len(s)
    #     dp = [1] * n
    #     for i in range(1,n):
    #         maxPre = 0
    #         for j in range(i):
    #             if isLegal(s[i],s[j]):
    #                 maxPre = max(maxPre,dp[j])
    #         dp[i] = maxPre+1
    #     return max(dp)
    
    # dp with hashmap, O(n)
    # def longestIdealString(self, s: str, k: int) -> int:
    #     c2lastIndex = {}
    #     n = len(s)
    #     dp = [1] * n # dp[i] means the ans end with s[:i+1]
    #     c2lastIndex[ord(s[0])-ord('a')] = 0
    #     for i in range(1,n):
    #         maxPre = 0
    #         val  = ord(s[i])-ord('a')
    #         for c in range(26):
    #             if c in c2lastIndex and abs(c-val) <= k:
    #                 maxPre = max(maxPre,dp[c2lastIndex[c]])
    #         dp[i] = maxPre+1
    #         c2lastIndex[val] = i
    #     return max(dp)
                
    # clever dp, just like use above hashmap as dp array, O(n)
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26 # dp[i] means the current ans when end with char i

        for c in s:
            maxPre = 0
            val = ord(c)-ord('a')
            for pre in range(26):
                if abs(pre-val) <= k:
                    maxPre = max(maxPre,dp[pre])
            dp[val] = maxPre+1
        return max(dp)

                