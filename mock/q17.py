from typing import List
class Solution:
    # O(n^2)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x:x[1])
        alive = [True]*n
        aliveCnt = n
        p = 0
        arrowCnt = 0
        while aliveCnt != 0:
            while not alive[p]:
                p += 1
            # kill this with its end
            # x b b b b
            # x T F -> F F
            arrowCnt += 1
            for i in range(p,n):
                if alive[i] and points[i][0]<=points[p][1]<=points[i][1]:
                    alive[i] = False
                    aliveCnt -= 1
        return arrowCnt
    
    # merge intervals,sort by start
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def isOverlap(a,b):
            if a[1]<b[0] or a[0]>b[1]:
                return False
            else:
                return True
            
        n = len(points)
        # sort by start or end both are ok
        # sort by start: if cur is not overlap with pre, then the following interval neither
        # but how sort by end works? there is a conter example:[1,2][3,4][2,5]
        # actually in first shoot, we can kill 2 balls; However in algorithm, we just kill one
        # (I am not sure about this point) we dont care [2,5] is killed by first or second shoot
        # because [2,5] must be covered by [3,4]: 
        # [2,5] is after [3,4] which means 5>4,
        # [2,5] overlap with [1,2] while [3,4] doot which means 2<3
        # so [2,5] must be covered by [3,4]
        # so all the intervals like [2,5] will be kill by following shoots
        points.sort() 
        cur = points[0]
        arrowCnt = 0
        for i in range(1,n):
            if isOverlap(cur,points[i]):
                cur = [max(cur[0],points[i][0]),min(cur[1],points[i][1])]
            else:
                arrowCnt += 1
                cur = points[i]
        return arrowCnt+1
    
    # sort by start
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        shoot = points[0][1]
        cnt = 0
        for start,end in points:
            if start>shoot:
                cnt += 1
                shoot = end
            else:
                shoot = min(shoot,end)
        return cnt+1
    
    # sort by end
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x:x[1])
        shoot = points[0][1]
        cnt = 0
        for start,end in points:
            if start>shoot:
                cnt += 1
                shoot = end
            else:
                # this sentence is useless as the curEnd is the smallest
                shoot = min(shoot,end)
        return cnt+1


        
