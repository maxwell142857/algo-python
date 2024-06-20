class Solution:
    # MLE, recursion with memo
    # def maximumTotalDamage(self, power: List[int]) -> int:
    #     n = len(power)
    #     val2cnt = defaultdict(int)
    #     for p in power:
    #         val2cnt[p] += 1

    #     maxP = max(power)

    #     memo = [[-1]*3 for _ in range(maxP+1)]

    #     def calculate(index,val):
    #         if index <0:
    #             return 0
    #         if memo[index][val] != -1:
    #             return memo[index][val]
            
    #         if val==0:
    #             # our bit is 00,so before can be (00)00,(01)00,(10)00
    #             memo[index][val] = max(calculate(index-2,0),calculate(index-2,1),calculate(index-2,2))
    #         elif val==1:
    #             # our bit is 01,so before can be (10)01,00(01)
    #             memo[index][val] = max(calculate(index-2,0),calculate(index-2,2))+index*val2cnt[index]
    #         elif val==2:
    #             # our bit is 10,so before can be (00)10
    #             memo[index][val] = calculate(index-2,0)+(index-1)*val2cnt[index-1]

    #         return memo[index][val]
    #     calculate(maxP,0)
    #     calculate(maxP,1)
    #     calculate(maxP,2)
    #     ans = 0
    #     for i in range(maxP+1):
    #         ans = max(ans,max(memo[i]))
    #     return ans
    
    # dp 
    def maximumTotalDamage(self, power: List[int]) -> int:
        val2cnt = defaultdict(int)
        vals = set()
        for p in power:
            val2cnt[p] += 1
            vals.add(p)
        vals = list(vals)
        vals.sort()
        n = len(vals)
        dp = [[0]*3 for _ in range(n)]
        ans = 0

        def getDP(i,j):
            if i>=0:
                return dp[i][j]
            else:
                return 0
            
        for i in range(n):
            dp[i][0] = max(getDP(i-2,0),getDP(i-2,1),getDP(i-2,2))
            dp[i%4][1] = i*val2cnt[i]+max(getDP(i-2,0),getDP(i-2,2))
            dp[i%4][2] = (i-1)*val2cnt[i-1]+getDP(i-2,0)
            ans = max(ans,max(dp[i%4]))
        return ans

            
