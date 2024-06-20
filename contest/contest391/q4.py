import heapq
class Solution:
    # use full heap ,MLE
    def minimumDistance(self, points: List[List[int]]) -> int:
        myHeap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                dis = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(myHeap,(-dis,i,j))
        ans = -myHeap[0][0]
        for i in range(n):
            # delete point with index i
            candidates = []
            while i == myHeap[0][1] or i == myHeap[0][2]:
                candidates.append(heapq.heappop(myHeap))
            ans = min(ans,-myHeap[0][0])
            # add back
            for candidate in candidates:
                heapq.heappush(myHeap,candidate)
        return ans
    
    # two heap, limit heap size to n, TLE
    def minimumDistance(self, points: List[List[int]]) -> int:
        minHeap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                dis = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(minHeap,(dis,i,j))
                if len(minHeap) > n:
                    heapq.heappop(minHeap)

        # convert minHeap to maxHeap
        maxHeap = []
        while minHeap:
            current = heapq.heappop(minHeap)
            heapq.heappush(maxHeap,(-current[0],current[1],current[2]))
        ans = -maxHeap[0][0]

        for i in range(n):
            # delete point with index i
            candidates = []
            while i == maxHeap[0][1] or i == maxHeap[0][2]:
                candidates.append(heapq.heappop(maxHeap))
            ans = min(ans,-maxHeap[0][0])
            # add back
            for candidate in candidates:
                heapq.heappush(maxHeap,candidate)
        return ans
    
    # heap + sort
    def minimumDistance(self, points: List[List[int]]) -> int:
        minHeap = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                dis = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(minHeap,(dis,i,j))
                if len(minHeap) > n:
                    heapq.heappop(minHeap)

        # convert minHeap to sorted array
        array = []
        while minHeap:
            array.append(heapq.heappop(minHeap))
        
        m = len(array)

        # try delete first index
        index = array[m-1][1]
        p = m-2
        while array[p][1] == index or array[p][2] == index:
            p -= 1
        tmpAns = array[p][0]
        # try delete second index
        index = array[m-1][2]
        p = m-2
        while array[p][1] == index or array[p][2] == index:
            p -= 1
        tmpAns = min(tmpAns,array[p][0])
        return tmpAns