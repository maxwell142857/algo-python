class Solution:
    # sort by end time + greedy
    # O(n^2)
    # TLE
    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     n = len(startTime)
    #     intervals = []
    #     for i in range(n):
    #         intervals.append([startTime[i],endTime[i],profit[i]])
    #     intervals.sort(key = lambda x:x[1])
    #     endTime2profit = {}
    #     for i in range(n):
    #         s,e,v = intervals[i]
    #         maxPre = 0
    #         for key,val in endTime2profit.items():
    #             if key <= s:
    #                 maxPre = max(maxPre,val)
    #         if e not in endTime2profit:
    #             endTime2profit[e] = maxPre+v
    #         else:
    #             endTime2profit[e] = max(endTime2profit[e],maxPre+v)
    #     return max(endTime2profit.values())


    # sort by end time+ binarySearch
    # key idea is dp,same as next solution
    # O(n*lgn)
    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     n = len(startTime)
    #     intervals = []
    #     for i in range(n):
    #         intervals.append([startTime[i],endTime[i],profit[i]])
    #     intervals.sort(key = lambda x:(x[1],x[0]))
    #     record = [] # (endTime,maxProfit), sort by endTime
    #     for i in range(n):
    #         s,e,v = intervals[i]
    #         # find the max endTime such that endTime <= start time
    #         # TTTFFF
    #         left = 0
    #         right = len(record)-1
    #         while left < right:
    #             mid = (left+right+1)//2
    #             if record[mid][0] <= s:
    #                 left = mid
    #             else:
    #                 right = mid-1
    #         if record and record[left][0] <= s:
    #             maxPre = record[left][1]
    #         else:
    #             maxPre = 0
            
    #         if record:
    #             record.append([e,max(record[-1][1],v+maxPre)])
    #         else:
    #             record.append([e,v+maxPre])

    #     ans = 0
    #     for e,v in record:
    #         ans = max(ans,v)
    #     return ans
    
    # sort by end time+ binarySearch+dp
    # O(n*lgn)
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = []
        for i in range(n):
            intervals.append([startTime[i],endTime[i],profit[i]])
        intervals.sort(key = lambda x:(x[1],x[0]))
        dp = [0]*n # dp[i] means max profit can get when finish i-th interval(not necessary include i-th)

        # find interval before such that interval's end time <= startT
        # return its val
        # if can not find, return 0
        # TTFFF
        # FFFFF
        def findPre(startT,endIndex):
            left = 0
            right = endIndex
            while left<right:
                mid = (left+right+1)//2
                if intervals[mid][1] <= startT:
                    left = mid
                else:
                    right = mid-1
            if intervals[left][1] <= startT:
                return dp[left]
            else:
                return 0
            
        dp[0] = intervals[0][2]
        for i in range(1,n):
            pre = findPre(intervals[i][0],i-1)
            dp[i] = max(dp[i-1],pre+intervals[i][2])
        return max(dp)
    
    # sort by start time + binary search + traverse with memo
    # O(n*lgn)
    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     n = len(startTime)
    #     intervals = []
    #     for i in range(n):
    #         intervals.append([startTime[i],endTime[i],profit[i]])
    #     intervals.sort(key = lambda x:x[0])

    #     def findNext(endTime,index):
    #         # FFFFFTTT
    #         # FFFFFFFF
    #         left = index
    #         right = n
    #         while left<right:
    #             mid = (left+right)//2
    #             if intervals[mid][0] >= endTime:
    #                 right = mid
    #             else:
    #                 left = mid+1
    #         if left == n:
    #             return -1
    #         else:
    #             return left
        
    #     memo = [-1]*n # memo[i] means start with index i, max profit can achieve

    #     def traverse(index):
    #         if index == n or index == -1:
    #             return 0
            
    #         if memo[index] != -1:
    #             return memo[index]
            
    #         memo[index] = max(traverse(index+1),intervals[index][2]+traverse(findNext(intervals[index][1],index+1)))
    #         return memo[index]
        
    #     return traverse(0)