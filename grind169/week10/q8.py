from collections import defaultdict,deque
class Solution:
    # 这个方法和方法二的区别是，方法二预先把图给build了，这样在BFS寻找下一个点的时候可以O(1)
    # 但这个方法必须首先得到当前线路的stop,然后对于每个stop，找到对应的route，所以更加耗时
    # 相当于方法二是预处理了
    # def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    #     if source==target:
    #         return 0
    #     node2routes = defaultdict(set)
    #     rCnt = len(routes)
    #     for i in range(rCnt):
    #         for node in routes[i]:
    #             node2routes[node].add(i)
        
    #     visited = set() # whether this route is visited
    #     queue = deque()
    #     cnt = 1
    #     for r in node2routes[source]:
    #         visited.add(r)
    #         queue.append(r)
    #         if r in node2routes[target]:
    #             return cnt
        
    #     # run BFS
    #     while queue:
    #         l = len(queue)
    #         cnt += 1
    #         for _ in range(l):
    #             rIndex = queue.popleft()
    #             stops = routes[rIndex]
    #             for s in stops:
    #                 for r in node2routes[s]:
    #                     if r not in visited:
    #                         visited.add(r)
    #                         queue.append(r)
    #                     if r in node2routes[target]:
    #                         return cnt
    #     return -1


    # prebuild the map, let the route be the node,save time
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        

        rCnt = len(routes)
        graph = [[] for _ in range(rCnt)]
        for i in range(rCnt):
            routes[i] = set(routes[i])
        
        def isConnect(i1,i2):
            r1 = routes[i1]
            r2 = routes[i2]
            for i in r1:
                if i in r2:
                    return True
            return False
        
        for i in range(rCnt):
            for j in range(i+1,rCnt):
                if isConnect(i,j):
                    graph[i].append(j)
                    graph[j].append(i)
        
        targetLines = set()
        for i in range(rCnt):
            if target in routes[i]:
                targetLines.add(i)
        
        # run BFS
        cnt = 1
        queue = deque()
        visited = set()
        for i in range(rCnt):
            if source in routes[i]:
                queue.append(i)
                visited.add(i)
                if i in targetLines:
                    return cnt
        
        while queue:
            cnt += 1
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                for neighbor in graph[cur]:
                    if neighbor in targetLines:
                        return cnt
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return -1
