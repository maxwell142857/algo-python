import heapq as h
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            h.heappush(self.minHeap,num)
            if len(self.minHeap) > k:
                h.heappop(self.minHeap)


    def add(self, val: int) -> int:
        h.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            h.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)