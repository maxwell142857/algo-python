class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inCount = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        for cur,pre in prerequisites:
            graph[pre].append(cur)
            inCount[cur] += 1
        level = []

        deletedCnt = 0
        ans = []
        for i in range(numCourses):
            if inCount[i] == 0:
                level.append(i)
                ans.append(i)
                deletedCnt += 1
        while level:
            tmp = level[:]
            level.clear()
            for node in tmp:
                sons = graph[node]
                for son in sons:
                    inCount[son] -= 1
                    if inCount[son] == 0:
                        level.append(son)
                        ans.append(son)
                        deletedCnt += 1
        if deletedCnt == numCourses:
            return ans
        else:
            return []
        