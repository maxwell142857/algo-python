from collections import defaultdict,deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def getTopoSort(conditions):
            inDegree = [0]*(k+1)
            map = defaultdict(list)
            queue = deque()
            for a,b in conditions:
                map[a].append(b)
                inDegree[b] += 1
            for i in range(1,k+1):
                if inDegree[i] == 0:
                    queue.append(i)
            index = 0
            val2index = {}

            while queue:
                cur = queue.popleft()
                val2index[cur] = index
                index += 1
                for son in map[cur]:
                    inDegree[son] -= 1
                    if inDegree[son] == 0:
                        queue.append(son)
            for i in range(1,k+1):
                if i not in val2index:
                    if inDegree[i] == 0:
                        val2index[i] = index
                        index += 1
                    else:
                        return None
            return val2index
        
        rowIndex = getTopoSort(rowConditions)
        colIndex = getTopoSort(colConditions)
        if not rowIndex or not colIndex:
            return []
        ans = [[0]*k for _ in range(k)]
        for i in range(1,k+1):
            
            r = rowIndex[i]
            c = colIndex[i]
            ans[r][c] = i
        return ans
            
            
            