class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        inDegree = [0]*n
        for a,b in roads:
            inDegree[a] += 1
            inDegree[b] += 1
        inDegree.sort()
        ans = 0
        for i in range(1,n+1):
            ans += inDegree[i-1]*i
        return ans