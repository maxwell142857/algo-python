# There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph 
# where graph[i] is an integer array of nodes adjacent to node i, 
# meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. 
# A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
# Example 2:

# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # dfs on each node to find whether it is in circle
        # if not, it is a safe node

        n = len(graph)
        ans = []
        visiting = [False]*n
        status = [0]*n # 0 for unvisited, 1 for safe, -1 for unsafe

        def checkCircle(current):
            if visiting[current]:
                status[current] = -1
                return True
            if status[current] != 0:
                return status[current]==-1
            
            visiting[current] = True
            haveCircle = False
            for sons in graph[current]:
                haveCircle |= checkCircle(sons)
            if haveCircle:
                status[current] = -1
            else:
                status[current] = 1
            visiting[current] = False

            return haveCircle


        for i in range(n):
            checkCircle(i)

        ans = []
        for i in range(n):
            if status[i] == 1:
                ans.append(i)
        return ans

        
    
    # def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        

    #     n = len(graph)
    #     sonTofather = [[] for _ in range(n)]
    #     for i in range(n):
    #         for son in graph[i]:
    #             sonTofather[son].append(i)

    #     deleted = set()

    #     level = []
    #     for i in range(n):
    #             if len(graph[i])==0:
    #                 level.append(i)
    #                 deleted.add(i)

    #     while level:
    #         tmp = level[:]
    #         level.clear()
    #         for node in tmp:
    #             fathers = sonTofather[node]
    #             for father in fathers:
    #                 graph[father].remove(node)
    #                 if not graph[father]:
    #                     level.append(father)
    #                     deleted.add(father)

    #     deleted = list(deleted)
    #     deleted.sort()
    #     return deleted


s = Solution()
graph1 = [[1,2],[2,3],[5],[0],[5],[],[]] # [2,4,5,6]
graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]] 
wrong = [[],[0,2,3,4],[3],[4],[]] # 1->2,3  2->3
print(s.eventualSafeNodes(wrong))
        