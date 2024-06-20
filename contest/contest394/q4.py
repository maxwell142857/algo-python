import heapq,random
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        m = len(edges)
        for i in range(m):
            a,b,val = edges[i]
            graph[a].append([b,val,i])
            graph[b].append([a,val,i])
        
        boolList = [False]*m
        ditance = [float('inf')]*n
        minHeap = [(0,0,[])] #(dis,nodeIndex,path)
        while minHeap:
            if minHeap[0][1] == n-1:
                dis = minHeap[0][0]
                while minHeap and minHeap[0][1] == n-1 and minHeap[0][0] == dis:
                    candidates = []
                    candidates.append(heapq.heappop(minHeap))
                    for cur in candidates:
                        for index in cur[2]:
                            boolList[index] = True
                return boolList
            cur = heapq.heappop(minHeap)
            if ditance[cur[1]] > cur[0]:
                ditance[cur[1]] = cur[0]
                for son in graph[cur[1]]:
                    newP = cur[2][:]
                    newP.append(son[2])
                    heapq.heappush(minHeap,(cur[0]+son[1],son[0],newP))
        return boolList
        
