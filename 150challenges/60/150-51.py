class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key = lambda x:x[1])
        n = len(points)
        i = 0
        while i < n:
            current = points[i]
            while i < n and points[i][0] <= current[1]:
                i += 1
            ans += 1
        return ans