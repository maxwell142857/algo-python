class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False

        dp = [[False]*(m+1) for _ in range(n+1)]
        # dp[i][j] mean s1 already use length i and s2 already use length j
        dp[0][0] = True
        for j in range(1,m+1):
            if s3[j-1] == s1[j-1] and dp[0][j-1]:
                dp[0][j] = True
        if n >=1:
            dp[1][0] = s3[0]==s2[0]

        for i in range(1,n+1):
            dp[i%2][0] = s3[i-1]== s2[i-1] and dp[(i-1)%2][0]
            for j in range(1,m+1):
                dp[i%2][j] = (dp[(i-1)%2][j] and s2[i-1] == s3[i+j-1]) or (dp[i%2][j-1] and s1[j-1] == s3[i+j-1])
        
        return dp[n%2][m]
        

