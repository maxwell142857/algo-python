class HitCounter:

    def __init__(self):
        self.t = []

    def hit(self, timestamp: int) -> None:
        self.t.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return self.firstGreater(timestamp)-self.firstGreater(timestamp-300)

    def firstGreater(self,val):
        left = 0
        right = len(self.t)
        while left < right:
            mid = (left+right)//2
            if self.t[mid]<=val:
                left = mid+1
            else:
                right = mid
        return left
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)