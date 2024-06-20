import heapq as h
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    # sort
    # O(n*log(n))
    # def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    #     timeLine = []

    #     for p in schedule:
    #         for interval in p:
    #             timeLine.append([interval.start,interval.end])
    #     timeLine.sort()
    #     ans = []
    #     pre = timeLine[0]
    #     for cur in timeLine[1:]:
    #         if cur[0]<=pre[1]:
    #             pre[1] = max(pre[1],cur[1])
    #         else:
    #             ans.append(Interval(pre[1],cur[0]))
    #             pre = cur
    #     return ans
    
    # use heap to merge k sorted list
    # O(n*log(k))
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        minHeap = [] # [start,peopleID,intervalID]
        peopleCnt = len(schedule)
        for i in range(peopleCnt):
            h.heappush(minHeap,(schedule[i][0].start,i,0))
        
        ans = []
        pre = None
        while minHeap:
            start,pID,iID = h.heappop(minHeap)
            if not pre:
                pre = schedule[pID][iID]
            else:
                if pre.end<start:
                    ans.append(Interval(pre.end,start))
                    pre = schedule[pID][iID]
                else:
                    pre.end = max(pre.end,schedule[pID][iID].end)
            if iID+1<len(schedule[pID]):
                h.heappush(minHeap,(schedule[pID][iID+1].start,pID,iID+1))
        return ans



        
