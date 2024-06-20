
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i:[] for i in range(numCourses)}
        candidate = []
        inCnt = {i:0 for i in range(numCourses)}
        deleteCnt = 0
        for start,end in prerequisites:
            edges[start].append(end)
            inCnt[end] += 1
        
        for i in range(numCourses):
            if inCnt[i] == 0:
                candidate.append(i)

        while candidate:
            current = candidate.pop()
            for to in edges[current]:
                inCnt[to] -= 1
                if inCnt[to] == 0:
                    candidate.append(to)
            deleteCnt += 1

        return deleteCnt == numCourses