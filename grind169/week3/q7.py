class Solution:
    # recursion with memo
    def coinChange(self, coins: List[int], amount: int) -> int:
        amount2cnt = {}

        def calculate(sum):
            if sum == 0:
                return 0
            if sum < 0:
                return float('inf')
            
            if sum in amount2cnt:
                return amount2cnt[sum]
            else:
                cnt = float('inf')
                for coin in coins:
                    val = calculate(sum-coin)+1
                    cnt = min(cnt,val)
                amount2cnt[sum] = cnt
                return amount2cnt[sum]
        
        result = calculate(amount)
        if result != float('inf'):
            return result
        else:
            return -1
    # dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin == 0:
                    dp[i] = 1
                elif i-coin > 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1