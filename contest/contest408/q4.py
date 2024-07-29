import math
class DSU:
    def __init__(self,n,x,y) -> None:
        # parent[n] is x = 0; parent[n+1] is y = 0
        # parent[n+2] is x = X; parent[n+3] is y = Y
        self.parent = [i for i in range(n+4)]
        self.x = x
        self.y = y

    def find(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        self.parent[pa] = pb

    def isConnect(self,a,b):
        return self.find(a) == self.find(b)

class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        def isOverlapping(c1,c2):
            dis1 = (c1[0]-c2[0])**2+(c1[1]-c2[1])**2
            dis2 = (c1[2]+c2[2])**2
            return dis1 <= dis2
        
        def connectX(c,x):

            # (c[0]-x)^2+(c[1]-y)^2 = c[2]^2
            # y in [0,Y]
            if (c[0]-x)**2>c[2]**2:
                return False
            y1 = c[1]+math.sqrt(c[2]**2-(c[0]-x)**2)
            y2 = c[1]-math.sqrt(c[2]**2-(c[0]-x)**2)
            if 0<=y1<=Y or 0<=y2<=Y:
                return True
            else:
                # check in circle
                if max(y1,y2)>Y and min(y1,y2)<0:
                    return True
                else:
                    return False
        
        def connectY(c,y):
            # (c[0]-x)^2+(c[1]-y)^2 = c[2]^2
            # x in [0,X]
            if (c[1]-y)**2>c[2]**2:
                return False
            
            x1 = c[0]+math.sqrt(c[2]**2-(c[1]-y)**2)
            x2 = c[0]-math.sqrt(c[2]**2-(c[1]-y)**2)
            if 0<=x1<=Y or 0<=x2<=Y:
                return True
            else:
                # check in circle
                if max(x1,x2)>X and min(x1,x2)<0:
                    return True
                else:
                    return False
        
            
        n = len(circles)
        dsu = DSU(n,X,Y)
        for i in range(n):
            for j in range(i):
                if isOverlapping(circles[i],circles[j]):
                    dsu.union(i,j)
            # connect 4 special line
            if connectX(circles[i],0):
                dsu.union(i,n)
            if connectX(circles[i],X):
                dsu.union(i,n+2)
            if connectY(circles[i],0):
                dsu.union(i,n+1)
            if connectY(circles[i],Y):
                dsu.union(i,n+3)
        if dsu.isConnect(n,n+1) or dsu.isConnect(n,n+2) or dsu.isConnect(n+1,n+3) or dsu.isConnect(n+2,n+3):
            return False
        else:
            return True
