class Solution:
    # greedy+sort
    # O(nlog(n))
    # def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    #     delta = []
    #     for num in nums:
    #         delta.append((num^k)-num)
    #     delta.sort(reverse = True)
    #     n = len(nums)
    #     ans = sum(nums)
    #     for i in range(0,n-1,2):
    #         pairVal = delta[i]+delta[i+1]
    #         if pairVal > 0:
    #             ans += pairVal
    #         else:
    #             break
    #     return ans
    
    # greedy+find min in positive and find max in negative
    # O(n)
    # def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    #     delta = []
    #     for num in nums:
    #         delta.append((num^k)-num)
    #     positiveCnt = 0
    #     positiveMin = float('inf')
    #     negativeMax = float('-inf')
    #     for val in delta:
    #         if val > 0:
    #             positiveCnt += 1
    #             positiveMin = min(positiveMin,val)
    #         else:
    #             negativeMax = max(negativeMax,val)
        
    #     ans = sum(nums)
    #     if positiveCnt%2 == 0:
    #         return ans+sum([val for val in delta if val > 0])
    #     else:
    #         if positiveMin+negativeMax>0:
    #             return ans+sum([val for val in delta if val > 0])+negativeMax
    #         else:
    #             return ans+sum([val for val in delta if val > 0])-positiveMin
            
    # dp
    # O(n)
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0]*n for _ in range(2)]
        # dp[0][j] means max val after deal j-th num, with legal parity
        # dp[1][j] means max val after deal j-th num, with illegal parity
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]^k
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1]+nums[i],dp[1][i-1]+(nums[i]^k))
            dp[1][i] = max(dp[1][i-1]+nums[i],dp[0][i-1]+(nums[i]^k))
        return dp[0][n-1]