class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        inDegree = defaultdict(int)
        for a,b in edges:
            inDegree[a] += 1
            inDegree[b] += 1
            if inDegree[a] > 1:
                return a
            if inDegree[b] > 1:
                return b 
