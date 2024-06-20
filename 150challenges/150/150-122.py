import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital,profits))
        projects.sort()
        
        heap = []
        index = 0
        
        for _ in range(k):
            while index< n and projects[index][0] <= w:
                heapq.heappush(heap,-projects[index][1])
                index += 1
            if len(heap) == 0:
                break
            w -= heapq.heappop(heap) # because the profit is negative
        
        return w