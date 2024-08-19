import heapq as h


class Solution:
    # use heap to record two smallest and largest
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = []
        maxVal = []

        for i,array in enumerate(arrays):
            h.heappush(minVal, (-array[0], i))
            if len(minVal) > 2:
                h.heappop(minVal)
                
            h.heappush(maxVal, (array[-1], i))
            if len(maxVal) > 2:
                h.heappop(maxVal)
        # 1 2 x x x 3 4
        val2, id2 = h.heappop(minVal)
        val1, id1 = h.heappop(minVal)
        val3, id3 = h.heappop(maxVal)
        val4, id4 = h.heappop(maxVal)
        if id1 != id4:
            return val1+val4
        else:
            return max(val1+val3,val2+val4)
        

    # more elegant
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        minVal,maxVal = arrays[0][0],arrays[0][-1]
        n = len(arrays)
        for i in range(1,n):
            ans = max(ans,arrays[i][-1]-minVal)
            ans = max(ans,maxVal-arrays[i][0])
            minVal = min(minVal,arrays[i][0])
            maxVal = max(maxVal,arrays[i][-1])
        return ans
            
        
