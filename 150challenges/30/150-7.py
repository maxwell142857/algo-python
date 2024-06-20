from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buyPrice = prices[0]
        profit = 0
        for i in range(1,n):
            profit = max(profit,prices[i]-buyPrice)
            buyPrice = min(buyPrice,prices[i])

        return profit

test = [7,1,5,3,6,4]
solution = Solution()
solution.maxProfit(test)