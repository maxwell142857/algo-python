class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # sumByLength[i] means the sum of subarr in length i
        sumByLength = [[] for _ in range(n+1)]
        for length in range(1,n+1):
            tmp = float("inf")
            for start in range(n):
                if start+length <= n:
                    if tmp == float("inf"):
                        tmp = sum(nums[start:start+length])
                    else:
                        tmp -= nums[start-1]
                        tmp += nums[start+length-1]
                    sumByLength[length].append(tmp)
                else:
                    break
        # maxVal[i][j] means the max sum of subarray in nums[i:j+1]
        maxVal = [[0]*n for _ in range(n)]
        minVal = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                candidates = []
                for length in range(n+1):
                    arr = sumByLength[length]
                    beforeCnt = i-length+1 
                    endCnt = j+1-length+1 
                    if beforeCnt>=0 and endCnt <= len(arr):
                        for index in range(beforeCnt,endCnt):
                            candidates.append(arr[index])
                candidates.sort()
                maxVal[i][j] = candidates[-1]
                minVal[i][j] = candidates[0]
        # dp[i][j] means end in i, we use j change
        dp = [[float('-inf')]*(k+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 0
        for j in range(1,k+1):
            for i in range(n):
                if j%2==0:
                    #find min
                    tmp = float('inf')
                    for before in range(i-1):
                        tmp = min(tmp,dp[before][k-1]+minVal[before+1][i])
                    dp[i][j] -= (k-j+1)*tmp
                else:
                    #find max
                    tmp = float('-inf')
                    for before in range(i-1):
                        tmp = max(tmp,dp[before][k-1]+maxVal[before+1][i])
                    dp[i][j] += (k-j+1)*tmp

        return dp[n-1][k]


        