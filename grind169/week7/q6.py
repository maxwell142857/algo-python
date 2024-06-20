class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def DFS(index):
            visited.add(index)
            for son in graph[index]:
                if son not in visited:
                    DFS(son)
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1
                DFS(i)
        return cnt