import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap,(-point[0]**2-point[1]**2,point[0],point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for element in heap:
            ans.append([element[1],element[2]])
        return ans