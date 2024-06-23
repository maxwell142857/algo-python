class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        start = 0
        cover = 0
        
        for i in range(start,start+minutes):
            cover += customers[i]
        coverMax = cover
        while start+minutes<n:
            cover -= customers[start]
            cover += customers[start+minutes]
            start += 1
            coverMax = max(coverMax,cover)
        return ans+coverMax