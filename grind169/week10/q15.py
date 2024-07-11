import heapq as h
class Solution:
    # O(nk*log(nk))
    # sliding windows
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        elements = []
        for i,l in enumerate(nums):
            for val in l:
                elements.append((val,i))
        elements.sort()

        cnt = len(elements)
        ans = [elements[0][0],elements[-1][0]]
        idCounter = defaultdict(int)
        left = 0
        for right in range(cnt):
            val,id = elements[right]
            idCounter[id] += 1
            while len(idCounter) == n:
                if idCounter[elements[left][1]] == 1:
                    # only this one remain, we should not shrink
                    break
                else:
                    idCounter[elements[left][1]] -= 1
                    left += 1
            if len(idCounter) == n and elements[right][0]-elements[left][0]<ans[1]-ans[0]:
                # update ans
                ans = [elements[left][0],elements[right][0]]
                
        return ans
    # O(nk*log(n))
    # heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        maxVal = -1
        
        for i,list in enumerate(nums):
            minHeap.append((list[0],i,0))
            maxVal = max(maxVal,list[0])
        h.heapify(minHeap)
        ans = [minHeap[0][0],maxVal]

        while True:
            val,id,p = h.heappop(minHeap)
            if p == len(nums[id])-1:
                # no more element to add
                break

            val = nums[id][p+1]
            h.heappush(minHeap,(val,id,p+1))
            maxVal = max(maxVal,val)

            if maxVal-minHeap[0][0]<ans[1]-ans[0]:
                ans = [minHeap[0][0],maxVal]
        return ans


