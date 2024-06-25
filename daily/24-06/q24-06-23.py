import heapq as h
from sortedcontainers import SortedDict
from collections import deque
class Solution:
    # binary search,TLE
    # between O(n*log(n)) and O(n^2*log(n))
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     n = len(nums)
    #     def check(l):
    #         for start in range(n):
    #             if start+l > n:
    #                 return False
    #             myMax = max(nums[start:start+l])
    #             myMin = min(nums[start:start+l])
    #             if myMax-myMin<=limit:
    #                 return True
        
    #     # use binary search
    #     # TTTFFFFF,TTTTT
    #     left = 1
    #     right = n
    #     while left<right:
    #         mid = (left+right+1)//2
    #         if check(mid):
    #             left = mid
    #         else:
    #             right = mid-1
    #     return left
    
    # sliding windows + two heap
    # O(n*lg(n))
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     n = len(nums)
    #     minHeap = [] # [val,timestamp]
    #     maxHeap = [] # [-val,timestamp]
    #     left = 0
    #     ans = 0
    #     for right in range(n):
    #         h.heappush(minHeap,(nums[right],right))
    #         h.heappush(maxHeap,(-nums[right],right))
    #         while -maxHeap[0][0]-minHeap[0][0] > limit:
    #             left += 1
    #             while maxHeap[0][1] < left:
    #                 h.heappop(maxHeap)
    #             while minHeap[0][1] < left:
    #                 h.heappop(minHeap)
    #         ans = max(ans,right-left+1)
    #     return ans
    
    # sortedDict (balanced BST)
    # O(n*lgn)
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     BST = SortedDict()
    #     n = len(nums)
    #     left = 0
    #     ans = 1
    #     for right in range(n):
    #         num =  nums[right]
    #         if num in BST:
    #             BST[num] += 1
    #         else:
    #             BST[num] = 1
            
    #         # check 
    #         while BST.peekitem(-1)[0]-BST.peekitem(0)[0]>limit:
    #             val = nums[left]
    #             BST[val] -= 1
    #             if BST[val] == 0:
    #                 BST.pop(val)
    #             left += 1
    #         ans = max(ans,right-left+1)
    #     return ans
    
    # monotonous deque
    # O(n)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minVal = deque() # ascending 
        maxVal = deque() # descending
        left = 0
        ans = 0
        n = len(nums)
        for right in range(n):
            val = nums[right]
            # update minVal
            while minVal and minVal[-1][0]>val:
                minVal.pop()
            minVal.append((val,right))
            # update maxVal
            while maxVal and maxVal[-1][0]<val:
                maxVal.pop()
            maxVal.append((val,right))

            # check 
            while maxVal[0][0]-minVal[0][0]>limit:
                if maxVal[0][1] == left:
                    maxVal.popleft()
                if minVal[0][1] == left:
                    minVal.popleft()
                left += 1
            
            ans = max(ans,right-left+1)
        return ans



