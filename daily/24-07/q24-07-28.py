from collections import defaultdict,deque
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        level = set()
        level.add(1)
        step = 0
        find = False
        distance = [-1]*(n+1)
        while not find:
            nextLevel = set()
            for cur in level:
                if distance[cur] == -1:
                    if cur == n:
                        find = True
                    distance[cur] = step
                elif step-distance[cur]>1:
                    continue

                
                for neighbor in graph[cur]:
                    nextLevel.add(neighbor)
            level = nextLevel
            step += 1
        if n not in level:
            distance[n] += 2
        else:
            distance[n] += 1
        # legal start time: 2k*change-3k*change
        total = 0
        for i in range(distance[n]):
            if (total//change)%2 == 0:
                # safe, can pass
                total += time
            else:
                total = (total//change+1)*change
                total += time
        return total

        



