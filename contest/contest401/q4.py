class Solution:
    # brute force 
    # TLE
    # def maxTotalReward(self, rewardValues: List[int]) -> int:
    #     rewardValues = list(set(rewardValues))
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
    # TLE
    # def maxTotalReward(self, rewardValues: List[int]) -> int:
    #     maxVal = 10**5
    #     rewardValues.sort()
    #     n = len(rewardValues)
    #     dp = [False]*maxVal
    #     dp[0] = True
    #     dp[rewardValues[0]] = True
    #     for i in range(1,n):
    #         for j in range(rewardValues[i]):
    #             if dp[j]:
    #                 dp[j+rewardValues[i]] = True
    #     ans = 0
    #     for j in range(maxVal):
    #         if dp[j]:
    #             ans = j
    #     return ans
    
    # dp in bitSet
    # bin(dp)[i] means i value can reach or not
    # to guarantee only choose preSum less than current val: dp&mask
    # to add current num: (xxxx<<num)
    # combine last state: dp = dp|xxxx
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        dp = 1<<0
        rewardValues = list(set(rewardValues))
        rewardValues.sort()
        for num in rewardValues:
            mask = (1<<(num))-1 
            dp = dp|((dp&mask)<<num)
        s = bin(dp)[2:]
        
        return len(s)-1

        