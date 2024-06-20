class DSU:
    def __init__(self,n) -> None:
        self.root = list(range(n))
    def find(self,x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,a,b):
        fa = self.find(a)
        fb = self.find(b)
        self.root[fa] = fb

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def from2to1(r,c):
            return r*n+c
        
        dsu = DSU(m*n)
        isLand = [[False]*n for _ in range(m)]
        ans = []
        tmpAns = 0
        for r,c in positions:
            if isLand[r][c] == True:
                ans.append(tmpAns)
                continue
            isLand[r][c] = True
            neighbor = [(0,1),(1,0),(0,-1),(-1,0)]
            neighborRoot = set()
            # calculate neighbor's root
            for i in range(4):
                rr = r+neighbor[i][0]
                cc = c+neighbor[i][1]
                if 0<=rr<m and 0<=cc<n and isLand[rr][cc]:
                    neighborRoot.add(dsu.find(from2to1(rr,cc)))
            # join neighbor
            for i in range(4):
                rr = r+neighbor[i][0]
                cc = c+neighbor[i][1]
                if 0<=rr<m and 0<=cc<n and isLand[rr][cc]:
                    dsu.union(from2to1(r,c),from2to1(rr,cc))
            # calculate new answer
            tmpAns += 1 # this new position
            tmpAns -= len(neighborRoot) # island deleted by add new position
            ans.append(tmpAns)
        return ans

                    
