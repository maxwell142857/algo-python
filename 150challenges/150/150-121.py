import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        cnt = 0
        for num in nums:
            heapq.heappush(heap,num)
            cnt += 1
            if cnt > k:
                heapq.heappop(heap)
                cnt -= 1
        return heap[-1]
