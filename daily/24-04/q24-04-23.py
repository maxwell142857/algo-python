class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        connectedCnt = [0]*n
        graph = defaultdict(list)
        for a,b in edges:
            connectedCnt[a] += 1
            connectedCnt[b] += 1
            graph[a].append(b)
            graph[b].append(a)
        deleteCnt = 0
        level = deque()
        for i in range(n):
            if connectedCnt[i] == 1:
                level.append(i)

        while deleteCnt < n-2:
            l = len(level)
            for _ in range(l):
                cur = level.popleft()
                connectedCnt[cur] = 0
                deleteCnt += 1
                for neibor in graph[cur]:
                    connectedCnt[neibor] -= 1
                    if connectedCnt[neibor] == 1:
                        level.append(neibor)
        return list(level)

