# recursive without memory, O(2^n)

# def findLength(s):
#     n = len(s)
#     # base case
#     if n==1:
#         return 1
#     if n==2 and s[0]==s[1]:
#         return 2
    
#     # recursive
#     if s[0] == s[n-1]:
#         # deal with the s.substring(1,n-1)
#         return findLength(s[1:n-1])+2
#     else:
#         # deal with the s.substring(0,n-1) or s.substring(1,n)
#         return max(findLength(s[0:n-1]),findLength(s[1:n]))


# recursive with memory,O(n^2)

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         memory = [[-1] * n for _ in range(n)]
#         return findLength(s,0,n-1,memory)
    
# def findLength(s,start,end,memory):
#     # first check memory
#     if memory[start][end] != -1:
#         return memory[start][end]
#     # base case
#     if start == end:
#         memory[start][end] = 1
#         return 1
#     if start+1 == end and s[start] == s[end]:
#         memory[start][end] = 2
#         return 2
    
#     # recursive
#     if s[start] == s[end]:
#         # deal with the s.substring(1,n-1)
#         memory[start][end] = findLength(s,start+1,end-1,memory)+2
#     else:
#         # deal with the s.substring(0,n-1) or s.substring(1,n)
#          memory[start][end] =  max(
#              findLength(s,start,end-1,memory),
#              findLength(s,start+1,end,memory))
#     return memory[start][end]

# dynamic programming

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                    
        return dp[0][n-1]
