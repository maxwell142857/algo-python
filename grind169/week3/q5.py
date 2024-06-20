from collections import deque


class Solution:
    # BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = {}
        inDegree  ={}
        for node1,node2 in prerequisites:
            if node1 not in edge:
                edge[node1] = [node2]
            else:
                edge[node1].append(node2)
            
            inDegree[node2] = inDegree.get(node2,0)+1
            inDegree[node1] = inDegree.get(node1,0)
        
        myDeque = deque()
        cnt = len(inDegree)
        for key,val in inDegree.items():
            if val == 0:
                myDeque.append(key)

        while myDeque:
            tmp = myDeque.popleft()
            cnt -= 1
            if tmp in edge:
                for son in edge[tmp]:
                    inDegree[son] -= 1
                    if inDegree[son] == 0:
                        myDeque.append(son)
            
        return cnt == 0
    
    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for node1,node2 in prerequisites:
            graph[node1].append(node2)
        
        findCircle = False
        visited = [False]*numCourses
        visiting = [False]*numCourses

        def DFS(current):
            nonlocal findCircle
            if findCircle:
                return
            if visiting[current]:
                findCircle = True
                return
            if visited[current]:
                return
            
            visiting[current] = True
            for son in graph[current]:
                DFS(son)

            visiting[current] = False
            visited[current] = True
        
        for i in range(numCourses):
            DFS(i)
        return not findCircle
            