# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
# you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# start DFS in each node,
# 1->3
# 1->2
# 3->4
# 4->2

from typing import List
from queue import Queue

class Solution:
    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = False
        graph = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        visited = [False]*numCourses
        checked = [False]*numCourses

        def DFS(node):
            nonlocal cycle 
            if checked[node]:
                return
            if visited[node]:
                cycle = True
                return
            visited[node] = True
            sons = graph[node]
            for son in sons:
                DFS(son)
                
            checked[node] = True

        for i in range(numCourses):
            if not checked[i]:
                DFS(i)
        return not cycle
   

    # BFS
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     edge = {} # int ->list,start -> many ends
    #     inCnt = [0] * numCourses
    #     for item in prerequisites:
    #         # start = item[0]
    #         # end = item[1]
    #         start = item[0]
    #         end = item[1]
    #         inCnt[end] += 1
    #         if start in edge:
    #             edge[start].append(end)
    #         else:
    #             edge[start] = [end]

    #     elementCnt = 0
    #     queue = Queue()
    #     for i in range(numCourses):
    #         if inCnt[i] == 0:
    #             queue.put(i)
    #     while queue.qsize() != 0:
    #         element = queue.get()
    #         elementCnt += 1
    #         if element in edge:
    #             sons = edge[element]
    #             for son in sons:
    #                 inCnt[son] -= 1
    #                 if inCnt[son] == 0:
    #                     queue.put(son)
    #     return elementCnt == numCourses

s = Solution()
print(s.canFinish(2,[[1,0],[0,1]]))