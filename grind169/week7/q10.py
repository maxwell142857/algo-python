import random
from collections import Counter
from typing import List
class Solution:

    def __init__(self, w: List[int]):
        
        self.n = len(w)
        self.preSum = [0]*self.n
        self.preSum[0] = w[0]

        for i in range(1,self.n):
            self.preSum[i] = self.preSum[i-1]+w[i]
        self.last = self.preSum[-1]
    def pickIndex(self) -> int:
        target = random.randint(1, self.last)
        # binary search, find first val greater than  or equal to target
        left = 0
        right = self.n-1
        while left < right:
            mid = (left+right)//2
            if self.preSum[mid] < target:
                left = mid+1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,4])
# 1,3,6,10
result = []
for _ in range(10000):
    result.append(obj.pickIndex())
print(Counter(result))