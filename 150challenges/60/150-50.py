class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ans = []
        dontAddIndex = set()
        newLeft = newInterval[0]
        newRight = newInterval[1]
        for i in range(n): 
            if not (intervals[i][1] < newInterval[0] or intervals[i][0] > newInterval[1]):
                dontAddIndex.add(i)
                newLeft = min(newLeft,intervals[i][0])
                newRight = max(newRight,intervals[i][1])

        
        for i in range(n):
            if i not in dontAddIndex:
                ans.append(intervals[i])
        added = False
        for i in range(len(ans)):
            if ans[i][0] > newLeft:
                    ans.insert(i,[newLeft,newRight])
                    added = True
                    break
        if not added:
            ans.append([newLeft,newRight])
        return ans