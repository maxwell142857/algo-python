class DSU:
    def __init__(self,n) -> None:
        self.father = [i for i in range(n)]
    
    def union(self,x,y):
        fx = self.find(x)
        fy = self.find(y)
        self.father[fx] = fy
    
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)

    def find(self,x):
        if self.father[x] !=x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Alice = DSU(n+1)
        Bob = DSU(n+1)
        shareCnt,aCnt,bCnt = 0,0,0
        # connect Type 3 edges 
        for t,x,y in edges:
            if t == 3:
                if not Alice.isConnected(x,y):
                    Alice.union(x,y)
                    Bob.union(x,y)
                    shareCnt += 1
        # connect type 1
        for t,x,y in edges:
            if t == 1:
                if not Alice.isConnected(x,y):
                    Alice.union(x,y)
                    aCnt += 1
        # connect type 2
        for t,x,y in edges:
            if t == 2:
                if not Bob.isConnected(x,y):
                    Bob.union(x,y)
                    bCnt += 1
        
        if shareCnt+aCnt==n-1 and shareCnt+bCnt==n-1:
            return len(edges)-shareCnt-aCnt-bCnt
        else:
            return -1

