import heapq as h
class MedianFinder:

    def __init__(self):
        self.maxH = [] # -val 
        self.minH = []

    def addNum(self, num: int) -> None:
        if not self.minH or num < self.minH[0]:
            # put into maxHeap
            h.heappush(self.maxH,-num)
            if len(self.maxH)-len(self.minH) == 2:
                h.heappush(self.minH,-h.heappop(self.maxH))
        else:
            # put into minHeap
            h.heappush(self.minH,num)
            if len(self.minH)-len(self.maxH) == 2:
                h.heappush(self.maxH,-h.heappop(self.minH))

    def findMedian(self) -> float:
        maxCnt = len(self.maxH)
        minCnt = len(self.minH)
        if maxCnt>minCnt:
            return -self.maxH[0]
        elif maxCnt==minCnt:
            return (-self.maxH[0]+self.minH[0])/2
        else:
            return self.minH[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()