class Solution:
    # dp 
    # def numDecodings(self, s: str) -> int:
    #     def isLegal(ss):
    #         if ss[0] == '0':
    #             return False
    #         val = int(ss)
    #         if 1<=val<=26:
    #             return True
    #         else:
    #             return False
        
    #     if s[0] == '0':
    #         return 0
        
    #     n = len(s) 
    #     dp = [0]*n # dp[i] means the way to decode when index is i
    #     dp[0] = 1
    #     if n >= 2:
    #         if s[1] != '0':
    #             dp[1] += 1
    #         if isLegal(s[:2]):
    #             dp[1] += 1
        
    #     for i in range(2,n):
    #         if s[i] != '0':
    #             dp[i] += dp[i-1]
    #         if isLegal(s[i-1:i+1]):
    #             dp[i] += dp[i-2]
    #     return dp[n-1]
    
    # dp with one more space in head, more elegant
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)
    #     dp = [0]*(n+1) # dp[i] means the way to decode when the length is i
    #     dp[0] = 1
    #     dp[1] = 1 if s[0] != '0' else 0
    #     for i in range(2,n+1):
    #         if s[i-1] != '0':
    #             dp[i] += dp[i-1]
    #         val = int(s[i-2:i])
    #         if 10<=val<=26:
    #             dp[i] += dp[i-2]
    #     return dp[n]
    
    # recursion with memo
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] *n

        def solve(index):
            if memo[index] != -1:
                return memo[index]
            
            if index == -1:
                return 1
            if index == 0:
                if s[0] != '0':
                    return 1
                else:
                    return 0
                
            ans = 0
            if s[index] != '0':
                ans += solve(index-1)
            if index-1 >= 0:
                val = int(s[index-1:index+1])
                if 10<=val<=26:
                    ans += solve(index-2)
            memo[index] = ans
            return ans
        
        return solve(len(s)-1)