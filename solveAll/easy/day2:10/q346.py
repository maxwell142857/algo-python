from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.list = deque()

    def next(self, val: int) -> float:
        self.list.append(val)
        self.sum += val
        if len(self.list)>self.size:
            self.sum -= self.list.popleft()
        return self.sum/len(self.list)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)