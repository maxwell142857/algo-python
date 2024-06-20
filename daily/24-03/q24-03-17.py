class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def checkOverlap(interval1,interval2):
            # if overlap, return the merge result
            if interval1[1]<interval2[0] or interval1[0]>interval2[1]:
                return []
            else:
                return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
            
        ans = []
        # merge
        for interval in intervals:
            result = checkOverlap(interval,newInterval)
            if result:
                newInterval = result
            else:
                ans.append(interval)
        # add newInterval
        n = len(ans)
        added = False
        for i in range(n):
            interval = ans[i]
            if interval[0]>newInterval[0]:
                ans.insert(i,newInterval)
                added = True
                break
        if not added:
            ans.append(newInterval)
        return ans