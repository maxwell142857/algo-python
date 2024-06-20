class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt = 0
        points.sort(key = lambda x:x[1])
        shotPoint = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] <= shotPoint:
                continue
            shotPoint = points[i][1]
            cnt += 1
        return cnt
