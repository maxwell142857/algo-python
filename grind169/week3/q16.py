class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def checkOverlap(interval1,interval2):
            if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
                return False
            else:
                return True
            
        def merge(interval1,interval2):
            return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
        
        intervals.sort()
        n = len(intervals)
        result = []
        current = intervals[0]
        index = 1
        while index < n:
            if checkOverlap(current,intervals[index]):
                current = merge(current,intervals[index])
                index += 1
            else:
                result.append(current)
                current = intervals[index]
                index += 1
        result.append(current)
        return result