from typing import List


class Solution:
    # def numberOfGoodPartitions(self, nums: List[int]) -> int:
    #     start = {}
    #     end = {}
    #     n = len(nums)
    #     for i in range(n):
    #         if nums[i] not in start:
    #             start[nums[i]] = i
    #         else:
    #             end[nums[i]] = i
    #     intervals = []

    #     for key in start.keys():
    #         if key in end:
    #             intervals.append([start[key],end[key]])
        
    #     newIntervals = []
    #     if len(intervals) != 0:
    #         intervals.sort(key=lambda x: x[0])
    #         intervalCnt = len(intervals)
    #         newIntervals.append(intervals[0])
    #         newIndex = 0
    #         for i in range(1,intervalCnt):
    #             if intervals[i][0] < newIntervals[newIndex][1]:
    #                 newIntervals[newIndex][1] = max(newIntervals[newIndex][1],intervals[i][1])
    #             else:
    #                 newIntervals.append(intervals[i])
    #                 newIndex += 1
        


    #     canUseCnt = n-1
    #     for interval in newIntervals:
    #         canUseCnt -= interval[1]-interval[0]
    #     ans = 1
    #     for i in range(canUseCnt):
    #         ans = ans * 2% (10**9 + 7)
    #     return ans
    
    # same thought, but more elegant
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        lastIndex = {x:i for i,x in enumerate(nums)}
        canUseCnt = 0
        last = 0
        for i in range(len(nums)-1):
            last = max(last,lastIndex[nums[i]])
            if i>=last: canUseCnt += 1
        return pow(2,canUseCnt,1_000_000_007)
    
s = Solution()
print(s.numberOfGoodPartitions([1,2,3,4]))