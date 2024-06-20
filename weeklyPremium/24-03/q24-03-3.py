import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heappush(heap,0)
        for interval in intervals:
            if interval[0] < heap[0]:
                #  we need a new room
                heapq.heappush(heap,interval[1])
            else:
                # use this exsiting room
                heapq.heappop(heap)
                heapq.heappush(heap,interval[1])
        return len(heap)
