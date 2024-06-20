
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i:[] for i in range(numCourses)}
        candidate = []
        inCnt = {i:0 for i in range(numCourses)}
        deleteCnt = 0
        ans = []
        for end,start in prerequisites:
            edges[start].append(end)
            inCnt[end] += 1
        
        for i in range(numCourses):
            if inCnt[i] == 0:
                candidate.append(i)

        while candidate:
            current = candidate.pop()
            ans.append(current)
            for to in edges[current]:
                inCnt[to] -= 1
                if inCnt[to] == 0:
                    candidate.append(to)
            deleteCnt += 1
        if deleteCnt == numCourses:
            return ans
        else:
            return []