#2024.1.13

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that 
# cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = []
        myDeque = deque(intervals)
        while myDeque:
            if len(myDeque) == 1:
                # only left one interval
                ans.append(myDeque.pop())
                break
            
            current = myDeque.popleft()
            next = myDeque.popleft()
            if current[1] < next[0]:
                # no overlap
                ans.append(current)
                myDeque.appendleft(next)
            else:
                # merge two intervals
                current = [current[0],max(current[1],next[1])]
                myDeque.appendleft(current)
        
        return ans

