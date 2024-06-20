class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        ans = 1
        visited = set()
        n = len(edges)+1
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def DFS(id):
            nonlocal ans
            if id in visited:
                return 0
            visited.add(id)
            length = []
            for sonID in graph[id]:
                length.append(DFS(sonID))
            length.sort(reverse=True)
            if len(length) == 1:
                ans = max(ans,length[0]+1)
                print((id,length[0]+1))
                return length[0]+1
            else:
                ans = max(ans,length[0]+length[1]+1)
                print((id,length[0]+length[1]+1))
                return length[0]+1
        
        DFS(0)
        return ans-1
