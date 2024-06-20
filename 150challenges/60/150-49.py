class Solution:
    # O(n^2) fail
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        ans = []
        tmp = []
        for item in intervals:
            newOne = [i for i in item]
            for interval in ans:
                if (newOne[0] <= interval[0] and interval[0]<=newOne[1]) or \
                    (newOne[0] <= interval[1]and interval[1]<=newOne[1]) or \
                    (newOne[0] <= interval[0]and interval[1]<=newOne[1]) or \
                    (newOne[0] >= interval[0]and interval[1]>=newOne[1])   :
                    newOne[0] = min(newOne[0],interval[0])
                    newOne[1] = max(newOne[1],interval[1])
                else:
                    tmp.append(interval)
            tmp.append(newOne)
            ans.clear()
            for t in tmp:
                ans.append([t[0],t[1]])
            tmp.clear()
        return ans
    # O(n*lgn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        if len(intervals) == 0:
            return []    
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        lastIndex = 0
        for i in range(1,len(intervals)):
            last = ans[lastIndex]
            if intervals[i][0]<= last[1]:
                ans[lastIndex][1] = max(ans[lastIndex][1],intervals[i][1])
            else:
                ans.append(intervals[i])
                lastIndex += 1
        return ans