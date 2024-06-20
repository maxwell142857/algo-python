from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buyPrice = prices[0]
        profit = 0
        for i in range(1,n):
            if prices[i] < prices[i-1]:
                profit += prices[i-1] - buyPrice
                buyPrice = prices[i]
        if prices[n-1] > buyPrice:
            profit += prices[n-1] - buyPrice
        return profit

test = [7,1,5,3,6,4]
solution = Solution()
solution.maxProfit(test)