class Solution:
    # divide-and-conquer O(n^2) TLE
    def maxProfit(self, prices: List[int]) -> int:
        def oneTimeBuy(start,end):
            if start >= n:
                return 0
            price = prices[start]
            profit = 0
            for i in range(start+1,end+1):
                profit = max(profit,prices[i]-price)
                price = min(price,prices[i])
            return profit

        n = len(prices)
        ans = 0
        for firstEnd in range(1,n):
            ans = max(ans,oneTimeBuy(0,firstEnd)+oneTimeBuy(firstEnd+1,n-1))
        return ans
    
    # dp, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        leftProfits = [0]*n
        price = prices[0]
        for i in range(1,n):
            leftProfits[i] = max(leftProfits[i-1],prices[i]-price)
            price = min(price,prices[i])
        
        rightProfits = [0]*(n+1)
        price = prices[n-1]
        for i in range(n-2,-1,-1):
            rightProfits[i] = min(rightProfits[i+1],prices[i]-price)
            price = max(price,prices[i])
        
        ans = 0
        for firstEnd in range(1,n):
            ans = max(ans,leftProfits[firstEnd]-rightProfits[firstEnd+1])
        return ans
