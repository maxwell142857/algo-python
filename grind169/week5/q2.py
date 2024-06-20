from collections import deque
class Solution:
    # O(n^2), TLE
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # check only one node
        if n==1:
            return [0]
        # build the map
        node2node = {}
        for a,b in edges:
            if a in node2node:
                node2node[a].append(b)
            else:
                node2node[a] = [b]
            if b in node2node:
                node2node[b].append(a)
            else:
                node2node[b] = [a]
        
        # run bfs on map, return the level
        def BFS(node):
            visited = set()
            level = [node]
            visited.add(node)
            cnt = 0
            while level:
                tmp = level[:]
                level.clear()
                for current in tmp:
                    for son in node2node[current]:
                        if son not in visited:
                            level.append(son)
                            visited.add(son)
                cnt += 1
            return cnt

        # BFS on each node
        cnt2node = {}
        for i in range(n):
            result = BFS(i)
            if result in cnt2node:
                cnt2node[result].append(i)
            else:
                cnt2node[result] = [i]
        
        # find the minmal cnt
        ansKey = n
        ansVal = []
        for key,val in cnt2node.items():
            if key < ansKey:
                ansKey = key
                ansVal = val
        return ansVal
        

    # two BFS to find the longest path, then one DFS to find the midpoint, O(n)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # check only one node
        if n==1:
            return [0]
        # build the map
        node2node = {}
        for a,b in edges:
            if a in node2node:
                node2node[a].append(b)
            else:
                node2node[a] = [b]
            if b in node2node:
                node2node[b].append(a)
            else:
                node2node[b] = [a]
        
        # run bfs on map, return the last level's node
        def BFS(node):
            visited = set()
            level = [node]
            visited.add(node)
            cnt = 0
            tmp = []
            while level:
                tmp = level[:]
                level.clear()
                for current in tmp:
                    for son in node2node[current]:
                        if son not in visited:
                            level.append(son)
                            visited.add(son)
                cnt += 1
            return tmp[0]
        
        
        start = BFS(0)
        end = BFS(start)
        
        ansPath = []
        visited = set()

        def DFS(path,target):
            nonlocal ansPath
            if ansPath:
                return
            
            if path[-1] == target:
                ansPath = path[:]
            
            current = path[-1]
            for son in node2node[current]:
                if son not in visited:
                    visited.add(son)
                    path.append(son)
                    DFS(path,target)
                    path.pop()
                    visited.remove(son)
        
        visited.add(start)
        DFS([start],end)
        length = len(ansPath)
        if length%2==0:
            return [ansPath[length//2],ansPath[length//2-1]]
        else:
            return [ansPath[length//2]]
    
    # similiar to toposort(BFS), O(n) 
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # check only one node
        if n==1:
            return [0]
        # build the map
        node2node = {}
        inDegree = [0]*n
        for a,b in edges:
            if a in node2node:
                node2node[a].append(b)
            else:
                node2node[a] = [b]
            if b in node2node:
                node2node[b].append(a)
            else:
                node2node[b] = [a]
            inDegree[a] += 1
            inDegree[b] += 1
        
        remainCnt = n
        candidates = []
        for i in range(n):
            if inDegree[i] == 1:
                candidates.append(i)
        while remainCnt > 2:
            tmp = candidates[:]
            candidates.clear()
            for candidate in tmp:
                inDegree[candidate] -= 1 # make it zero
                remainCnt -= 1
                for son in node2node[candidate]:
                    if inDegree[son]!=0:
                        inDegree[son] -= 1
                        if inDegree[son] == 1:
                            candidates.append(son)
        return candidates
            

