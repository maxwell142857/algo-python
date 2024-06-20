class DSU:
    def __init__(self,n) -> None:
        self.n = n
        self.father = list(range(n))
        self.rank = [1]*n
    
    def find(self,a):
        if self.father[a] != a:
            self.father[a] = self.find(self.father[a])
        return self.father[a]
    
    def union(self,a,b):
        fa = self.find(a)
        fb = self.find(b)
        if fa == fb:
            return
        # to guarantee tree a is small
        if self.rank[fa] > self.rank[fb]:
            fa,fb = fb,fa
        self.father[fa] = fb
        self.rank[fb] += self.rank[fa]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = DSU(n)
        for a,b in edges:
            dsu.union(a,b)
        return dsu.find(source) == dsu.find(destination)