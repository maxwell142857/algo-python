class Solution:
    # O(n^2),DFS on each node, TLE
    # def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    #     graph = defaultdict(list)
    #     for a,b in edges:
    #         graph[a].append(b)
    #         graph[b].append(a)
        
    #     pathSum = 0
    #     visited = set()
    #     def DFS(node,pathLength):
    #         nonlocal pathSum,visited
    #         pathSum += pathLength
    #         visited.add(node)
    #         for neighbor in graph[node]:
    #             if neighbor not in visited:
    #                 DFS(neighbor,pathLength+1)
        
    #     ans = []
    #     for i in range(n):
    #         pathSum = 0
    #         visited = set()
    #         DFS(i,0)
    #         ans.append(pathSum)
    #     return ans


# thought
# Disconnecting any edge, say [i, j], would break the tree into two subtrees, one with node i and another with node j
# Use count[i,j] to represent the number of nodes in subtree with node i if edge [i, j] was disconnected. Then count[j,i] = N - count[i,j]
# For any adjacent node pair i and j: sum[j] = sum[i] - count[j,i] + count[i,j]
# Calculate sum of distance for one arbitrary node, and use the fomula to calculate the others.

    # O(n)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # build graph, O(n)
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # calculate count[(i,j)]
        cnt = {}
        visited = set()
        def subTreeSize(cur):
            visited.add(cur)
            mySize = 1
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    size = subTreeSize(neighbor)
                    cnt[(neighbor,cur)] = size
                    cnt[(cur,neighbor)] = n-size
                    mySize += size
            return mySize
        subTreeSize(0)

        # calculate sum[0]
        sum0 = 0
        visited = set()
        def findPathSum(node,pathLength):
            nonlocal sum0,visited
            sum0 += pathLength
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    findPathSum(neighbor,pathLength+1)
        findPathSum(0,0)

        # Calculate sum for all other nodes
        ans = [0]*n
        ans[0] = sum0
        visited = set()
        def DFS(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    ans[neighbor] = ans[node]+cnt[(node,neighbor)]-cnt[(neighbor,node)]
                    DFS(neighbor)
        DFS(0)
        return ans