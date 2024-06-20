import heapq as h
class Solution:
    # search,O(n*2^n), TLE
    # def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    #     n = len(quality)
    #     indexs = []
    #     ans = float('inf')
    #     def backtracking(p):
    #         nonlocal ans
    #         if len(indexs) == k:
    #             # calculate the cost
    #             cost = 0
    #             perPrice = max(wage[index]/quality[index] for index in indexs)
    #             for index in indexs:
    #                 cost += max(wage[index],perPrice*quality[index])
    #             ans = min(ans,cost)
    #             return
            
    #         if p == n:
    #             return
            
    #         backtracking(p+1)
    #         indexs.append(p)
    #         backtracking(p+1)
    #         indexs.pop()
        
    #     backtracking(0)
    #     return ans

    # sort + heap
    # O(n*logn+n*logk)
    # sort by ratio
    # travere the sorted array, maintain heap by quality
    # def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    #     n = len(quality)
    #     arr = [(wage[i]/quality[i],quality[i]) for i in range(n)]
    #     arr.sort()

    #     maxHeap = []
    #     ratio,totalQuality = 0,0
    #     ans =  float('inf')
    #     for i in range(n):
    #         ratio = arr[i][0]
    #         totalQuality += arr[i][1]
    #         h.heappush(maxHeap,-arr[i][1])
    #         if len(maxHeap)>k:
    #             totalQuality += h.heappop(maxHeap)
    #         if len(maxHeap) == k:
    #             ans = min(ans,ratio*totalQuality)
    #     return ans
    
    # sort + heap
    # O(n*logn+n*(k+logk))
    # sort by quality
    # travere the sorted array, maintain heap by ratio
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        arr = [(quality[i],wage[i]/quality[i]) for i in range(n)]
        arr.sort()

        maxHeap = []
        totalQuality = 0
        ans =  float('inf')
        for i in range(n):
            totalQuality += arr[i][0]
            h.heappush(maxHeap,(-arr[i][1],arr[i][0]))
            if len(maxHeap)>k:
                delete = h.heappop(maxHeap)
                totalQuality -= delete[1]
            if len(maxHeap) == k:
                maxRatio = -min(x[0] for x in maxHeap) # O(k)
                ans = min(ans,maxRatio*totalQuality)
        return ans
                        
