from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        arr = []
        for k,v in count.items():
            arr.append((k,v))
        arr.sort()
        n = len(arr)
        dp = [0]*n
        dp[0] = arr[0][0]*arr[0][1]
        for i in range(1,n):
            curVal = arr[i][0]
            dp[i] = curVal*arr[i][1]
            preIndex = i-1
            while preIndex>=0 and curVal-arr[preIndex][0]<=2:
                preIndex -= 1
            if preIndex >= 0:
                dp[i] += dp[preIndex]
            # or just skip this spell
            dp[i] = max(dp[i],dp[i-1])
        return max(dp)