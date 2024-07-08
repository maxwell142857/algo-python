class DSU:
    def __init__(self,n) -> None:
        self.father = [i for i in range(n)]
        self.rank = [0]*n
    
    def union(self,a,b):
        fa = self.find(a)
        fb = self.find(b)
        if fa==fb:
            return False
        else:
            if self.rank[fa] >self.rank[fb]:
                self.father[fb] = fa
                self.rank[fa] += self.rank[fb]
            else:
                self.father[fa] = fb
                self.rank[fb] += self.rank[fa]
            return True

    def find(self,a):
        if self.father[a] != a:
            self.father[a] = self.find(self.father[a])
        return self.father[a]
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        edgeCnt = 0
        logs.sort()
        dsu = DSU(n)
        for time,a,b in logs:
            if dsu.union(a,b):
                edgeCnt += 1
                if edgeCnt == n-1:
                    return time
        return -1
