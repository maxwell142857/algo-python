from collections import deque,defaultdict
import heapq
class Solution:
    # BFS + pruning
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    #     graph = defaultdict(list)
    #     for a,b,c in flights:
    #         graph[a].append((b,c))
    #     distance = [float('inf')]*n
    #     distance[src] = 0
    #     level = deque()
    #     level.append((src,0))
    #     if src == dst:
    #         return 0
        
    #     for _ in range(k+1):
    #         length = len(level)
    #         for _ in range(length):
    #             cur,val = level.popleft()
    #             for node,dis in graph[cur]:
    #                 if dis+val<distance[node]:
    #                     distance[node] = dis+val
    #                     # level.append((node,distance[node]))
                    
    #                 # if we write here, we get MLE
    #                 # write it in the if condition as pruning
    #                 # level.append((node,distance[node]))

    #     if distance[dst] == float('inf'):
    #         return -1
    #     else:
    #         return distance[dst]

    # djstra+ pruning
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,c in flights:
            graph[a].append((b,c))
        minHeap = [(0,src,0)] # distance to this node, nodeID, step used

        minStep = [float('inf')]*n
        # record each node's step we arrive it
        # when run djstra, we visit node by ditance
        # if the step > minStep[i], we do not need to continue this path 
        while minHeap:
            distance,node,used = heapq.heappop(minHeap)
            if node == dst:
                return distance
            # pruning
            if minStep[node] <= used:
                continue
            else:
                minStep[node] = used

            if used < k+1:
                for next,path in graph[node]:
                    heapq.heappush(minHeap,(distance+path,next,used+1))
        return -1
    
    # 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            

