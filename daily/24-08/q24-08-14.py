import heapq as h
class Solution:
    # heap, O(n^2 logK), TLE
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n  = len(nums)
        maxHeap = []
        for i in range(n):
            for j in range(i+1,n):
                val = abs(nums[i]-nums[j])
                h.heappush(maxHeap,-val)
                if len(maxHeap)>k:
                    h.heappop(maxHeap)
        return -maxHeap[0]

    # merge k sorted list,O(k*n*logn), TLE
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        minHeap = [] # curVal,end
        for i in range(1,n):
            minHeap.append((nums[i]-nums[i-1],i))
        h.heapify(minHeap)
        for i in range(k-1):
            val,index = h.heappop(minHeap)
            if index != n-1:
                h.heappush(minHeap,(val+nums[index+1]-nums[index],index+1))
        return minHeap[0][0]
    
    # binary search + sliding windows
    # O(nlogn+n*log(max(nums)))
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        def count(d):
            cnt = 0
            left = 0
            for right in range(n):
                while nums[right]-nums[left] > d:
                    left += 1
                cnt += right-left
            return cnt

        lo = 0
        hi = max(nums)
        # FFFTTTT
        while lo<hi:
            mid = (lo+hi)//2
            if count(mid)>=k:
                hi = mid
            else:
                lo = mid+1
        return lo