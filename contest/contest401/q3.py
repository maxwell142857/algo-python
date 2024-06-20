class Solution:
    # brute force
    # O(2^n)?
    # def maxTotalReward(self, rewardValues: List[int]) -> int:
    #     rewardValues.sort()
    #     pre = set()
    #     pre.add(0)
    #     for r in rewardValues:
    #         tmp = set()
    #         for val in pre:
    #             if val < r:
    #                 tmp.add(val+r)
    #         pre = pre|tmp
    #     return max(pre)


    # dp
    # O(4000*n)
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        n = len(rewardValues)
        dp = [False]*4000
        dp[0] = True
        dp[rewardValues[0]] = True
        for i in range(1,n):
            for j in range(rewardValues[i]):
                if dp[j]:
                    dp[j+rewardValues[i]] = True
        ans = 0
        for j in range(4000):
            if dp[j]:
                ans = j
        return ans