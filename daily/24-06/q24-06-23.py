import heapq as h
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
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minHeap = [] # [val,timestamp]
        maxHeap = [] # [-val,timestamp]
        left = 0
        ans = 0
        for right in range(n):
            h.heappush(minHeap,(nums[right],right))
            h.heappush(maxHeap,(-nums[right],right))
            while -maxHeap[0][0]-minHeap[0][0] > limit:
                left += 1
                while maxHeap[0][1] < left:
                    h.heappop(maxHeap)
                while minHeap[0][1] < left:
                    h.heappop(minHeap)
            ans = max(ans,right-left+1)
        return ans
