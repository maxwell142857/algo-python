class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def isOverlap(a,b):
            if a[1] <= b[0] or a[0] >= b[1]:
                return False
            else:
                return True
        intervals.sort(key = lambda x:x[1])

        n  =len(intervals)
        lastVal = -float('inf')
        cnt = 0
        for start,end in intervals:
            if start >= lastVal:
                cnt += 1
                lastVal = end
        return n-cnt

