# implement by heap
# push and pop in O(lg(n))
# as we need to get the max frequency with max timestamp
# just combine these two informations into a HeapNode and put it into heap
# but when we push, the node needs to update?
# just add new node, and keep the old node in heap
# the node represents the state: when you pop the new added element, the old node is the old state
    
import heapq as h
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.maxHeap = []
        self.val2f = defaultdict(int)
        self.timestamp = 0

    def push(self, val: int) -> None:
        self.val2f[val] += 1
        h.heappush(self.maxHeap,(-self.val2f[val],-self.timestamp,val))
        self.timestamp += 1
        

    def pop(self) -> int:
        f,t,val = h.heappop(self.maxHeap)
        self.val2f[-val] -= 1
        return val
            
                


# dict with stack
# O(1)
# we dont need heap
# supppose the current max frequency is k
# the next max frequency must be k or k-1 (next pointer is continuous)
# class FreqStack:

#     def __init__(self):
#         self.val2f = defaultdict(int)
#         self.f2vals = defaultdict(list)
#         self.maxF = 0


#     def push(self, val: int) -> None:
#         self.val2f[val] += 1
#         self.f2vals[self.val2f[val]].append(val)
#         self.maxF = max(self.maxF,self.val2f[val])

#     def pop(self) -> int:
#         ans = self.f2vals[self.maxF].pop()
#         self.val2f[ans] -= 1
#         if len(self.f2vals[self.maxF]) == 0:
#             self.maxF -= 1
#         return ans
