class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = [False]*n
        map = defaultdict(list)
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)
        
        def DFS(cur):
            visited[cur] = True
            sons = map[cur]
            for son in sons:
                if not visited[son]:
                    DFS(son)
        
        DFS(0)
        for v in visited:
            if not v:
                return False
        return True

