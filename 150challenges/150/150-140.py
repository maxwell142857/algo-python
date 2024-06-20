class Solution:
    # top-down dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        for coin in coins:
            memo[coin] = 1
        
        def getCnt(money):
            if money < 0:
                return float("inf")
            if money in memo:
                return memo[money]
            
            tmp = float("inf")
            for coin in coins:
                tmp = min(tmp,getCnt(money-coin)+1)
            memo[money] = tmp
            return tmp
        
        result = getCnt(amount)
        if result == float("inf"):
            return -1
        else:
            return result
    
    # bottom-up dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin > 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]