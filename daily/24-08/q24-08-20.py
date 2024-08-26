class Solution:
    # O(n^2)
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        suffixSum = piles[:]
        for i in range(n-2,-1,-1):
            suffixSum[i] += suffixSum[i+1]
        memo = [[-1]*n for _ in range(n)]
        def solve(start,M):
            if n-start <=2*M:
                return suffixSum[start]
            if memo[start][M] != -1:
                return memo[start][M]

            for x in range(1,2*M+1):
                myTake = suffixSum[start]-suffixSum[start+x]
                nextTake = suffixSum[start+x]-solve(start+x,max(M,x))
                memo[start][M] = max(memo[start][M],myTake+nextTake)
            return memo[start][M]
        return solve(0,1)
