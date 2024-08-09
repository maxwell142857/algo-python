class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intervalOverlap(a,b):
            if a[0]>=b[1] or a[1]<=b[0]:
                return False
            else:
                return True
        rec1X = [rec1[0],rec1[2]]
        rec1Y = [rec1[1],rec1[3]]
        rec2X = [rec2[0],rec2[2]]
        rec2Y = [rec2[1],rec2[3]]
        return intervalOverlap(rec1X,rec2X) and intervalOverlap(rec1Y,rec2Y)
    