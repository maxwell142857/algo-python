import heapq as h
from collections import deque
class Solution:
    # use heap, there are some fake node in heap. Distinguish them by timestamp
    # avg: O(n*lgk),worst:O(n*lgn) I am not sure, this solutiom's TC is tricky
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     maxHeap = [] # [-val,index] use index to judge expired
    #     ans = []
    #     n = len(nums)
    #     for i in range(n):
    #         val = nums[i]
    #         h.heappush(maxHeap,[-val,i])
    #         if len(maxHeap)>=k:
    #             while maxHeap[0][1]<=i-k:
    #                 h.heappop(maxHeap)
    #             ans.append(-maxHeap[0][0])
    #     return ans
                

    # monotonous stack, store val and index
    # O(n)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     descStack = deque() #(val,index)
    #     ans = []
    #     for i in range(n):
    #         while descStack and descStack[-1][0] <= nums[i]:
    #             descStack.pop()
    #         descStack.append((nums[i],i))
    #         while descStack[0][1]<=i-k:
    #             descStack.popleft()
    #         if i >= k-1:
    #             ans.append(descStack[0][0])
    #     return ans
    
    # monotonous stack, only store index
    # O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        descStack = deque() # index
        ans = []
        for i in range(n):
            while descStack and nums[descStack[-1]] <= nums[i]:
                descStack.pop()
            descStack.append(i)
            if descStack[0] == i-k:
                descStack.popleft()
            if i >= k-1:
                ans.append(nums[descStack[0]])
        return ans