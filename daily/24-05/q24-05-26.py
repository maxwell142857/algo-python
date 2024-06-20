class Solution:
    # recursion with memo,implemented by dict
    # O(n)
    # MLE
    # the lesson is, do not implement memo by dict
    # def checkRecord(self, n: int) -> int:
    #     mod = 10**9+7
    #     memo = {}
    #     def construct(index,aCnt,l):
    #         if (index,aCnt,l) in memo:
    #             return memo[(index,aCnt,l)]
            
    #         if aCnt == 2 or l == 3:
    #             return 0
            
    #         if index == n:
    #             return 1
            
    #         # choose A 
    #         tmp1 = construct(index+1,aCnt+1,0)
    #         # choose L 
    #         tmp2 = construct(index+1,aCnt,l+1)
    #         # choose P
    #         tmp3 = construct(index+1,aCnt,0)

    #         memo[(index,aCnt,l)] = (tmp1+tmp2+tmp3)%mod
    #         return memo[(index,aCnt,l)]
        
    #     return construct(0,0,0)


    # recursion with memo, implemented by 3d array
    # O(n)
    # pass
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        memo = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        def construct(index,aCnt,l):
            if aCnt == 2 or l == 3:
                return 0
            
            if index == n:
                return 1
            
            if memo[index][aCnt][l] != -1:
                return memo[index][aCnt][l]
            
            
            
            # choose A 
            tmp1 = construct(index+1,aCnt+1,0)
            # choose L 
            tmp2 = construct(index+1,aCnt,l+1)
            # choose P
            tmp3 = construct(index+1,aCnt,0)

            memo[index][aCnt][l] = (tmp1+tmp2+tmp3)%mod
            return memo[index][aCnt][l]
        
        return construct(0,0,0)
    

    # dp
    # O(n)
    # pass
    # def checkRecord(self, n: int) -> int:
    #     mod = 10**9+7
    #     # dp[i][j][k]
    #     # i for index,j for aCnt(0,1), k for consecutive late(0,1,2)
    #     dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        
    #     # choose A to reach current situation: dp[i-1][j-1][0,1,2] -> dp[i][j][k=0]
    #     # choose L to reach current situation: dp[i-1][j][k-1] -> dp[i][j][k]
    #     # choose P to reach current situation: dp[i-1][j][0,1,2] ->dp[i][j][k=0]
    #     dp[0][0] = [1,1,0]
    #     dp[0][1] = [1,0,0]
    #     for i in range(1,n):
    #         dp[i][0][0] = sum(dp[i-1][0])%mod # choose P
    #         dp[i][0][1] = dp[i-1][0][0] # choose L
    #         dp[i][0][2] = dp[i-1][0][1] # choose L 
    #         dp[i][1][0] = (sum(dp[i-1][1])%mod+sum(dp[i-1][0])%mod)%mod # choose P or A
    #         dp[i][1][1] = dp[i-1][1][0] # choose L
    #         dp[i][1][2] = dp[i-1][1][1] # choose L 
        
    #     return (sum(dp[n-1][0])+sum(dp[n-1][1]))%mod