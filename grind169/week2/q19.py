class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def check(interval1,interval2):
            if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
                return False
            else:
                return True
        
        def merge(interval1,interval2):
            return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
        
        ans = []
        for interval in intervals:
            if check(interval,newInterval):
                newInterval = merge(newInterval,interval)
            else:
                ans.append(interval)
        added = False
        for i in range(len(ans)):
            if newInterval[0] < ans[i][0]:
                ans.insert(i,newInterval)
                added = True
                break
        if not added:
            ans.append(newInterval)
        return ans
