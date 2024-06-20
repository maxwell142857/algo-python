from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowCnt = len(mat)
        colCnt = len(mat[0])
        ans = [[-1]*colCnt for _ in range(rowCnt)]
        distance = 0
        queue = []
        visited = set()
        for r in range(rowCnt):
            for c in range(colCnt):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
                    
        while queue:
            tmp = queue[:]
            queue.clear()
            for item in tmp:
                ans[item[0]][item[1]] = distance
                
                bias_r = [0,0,1,-1]
                bias_c = [1,-1,0,0]
                for i in range(4):
                    newR = item[0]+bias_r[i]
                    newC = item[1]+bias_c[i]
                    if 0<=newR<rowCnt and 0<=newC<colCnt and (newR,newC) not in visited:
                        queue.append([newR,newC])
                        visited.add((newR,newC))
            distance += 1
        return ans
    