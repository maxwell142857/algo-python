class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        squares = sorted(zip(bottomLeft,topRight))
        ansSize = 0
        for i in range(n):
            for j in range(i+1,n):
                ax1,ay1 = squares[i][0]
                ax2,ay2 = squares[i][1]
                bx1,by1 = squares[j][0]
                bx2,by2 = squares[j][1]
                xOverlapping = min(ax2,bx2)-max(ax1,bx1)
                yOverlapping = min(ay2,by2)-max(ay1,by1)

                if xOverlapping>0 and yOverlapping>0:
                    ansSize = max(ansSize,min(xOverlapping,yOverlapping))
                elif xOverlapping<0 and yOverlapping<0:
                    break
        
        return ansSize**2
