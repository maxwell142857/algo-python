import heapq as h
class Solution:
    # heap,O(X+Klog(X)),X=min(K,N)
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     n = len(matrix)
    #     minHeap = [] #(val,i,j)
    #     for i in range(min(n,k)):
    #         minHeap.append((matrix[i][0],i,0))
    #     h.heapify(minHeap)
    #     for _ in range(k-1):
    #         val,i,j = h.heappop(minHeap)
    #         if j != n-1:
    #             h.heappush(minHeap,(matrix[i][j+1],i,j+1))
    #     return minHeap[0][0]
    
    # Bsearch,O(N×log(Max−Min))
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def getCnt(val):
            maxVal = float('-inf')
            cnt = 0
            c = n-1
            for r in range(n):
                while c >=0 and matrix[r][c] > val:
                    c -= 1
                cnt += c+1
                if c == -1:
                    break
                maxVal = max(maxVal,matrix[r][c])
            return [cnt,maxVal]
        
        left = min(min(row) for row in matrix)-1
        right = max(max(row) for row in matrix)+1
        ans = 0
        while left < right:
            mid = (left+right)//2
            result = getCnt(mid)
            if result[0] >= k:
                right = mid
                ans = result[1]
            else:
                left = mid+1
        return ans