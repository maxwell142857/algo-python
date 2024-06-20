import heapq as h
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        projects = []
        n = len(profits)
        for i in range(n):
            projects.append([capital[i],profits[i]])
        projects.sort()
        p = 0
        cnt = 0
        while cnt < k:
            while p<n and projects[p][0]<=w:
                h.heappush(maxHeap,-projects[p][1])
                p += 1
            if not maxHeap:
                break
            w -= h.heappop(maxHeap)
            cnt += 1
        return w