import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        minHeap  = []
        for start,end in intervals:
            if not minHeap:
                minHeap.append(end)
            else:
                if start >= minHeap[0]:
                    # use this room
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap,end)
                else:
                    # need a new room
                    heapq.heappush(minHeap,end)
                
        return len(minHeap)

