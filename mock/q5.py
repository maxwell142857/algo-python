# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 
# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

# n intervals,sort by start,
# heap store room's end time,little head heap,

import heapq
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the interval by start time
        intervals.sort()
        myheap = [0]
        heapq.heapify(myheap)

        for start, end in intervals:
            # get the earliest room
            tmp = myheap[0]
            if tmp <= start:
                # use this room
                heapq.heappop(myheap)
                heapq.heappush(myheap,end)
            else:
                # need a new room
                heapq.heappush(myheap,end)
        return len(myheap)



s = Solution()
test1 = [[0,30],[5,10],[15,20]] # 2
test2 = [[7,10],[2,4]]  # 1
print(s.minMeetingRooms(test1)==2)
print(s.minMeetingRooms(test2)==1)
