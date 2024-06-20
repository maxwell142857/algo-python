from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        visitied = set()
        level = []
        # find the start
        for r in range(rowCnt):
            if level:
                break
            for c in range(colCnt):
                if grid[r][c] == '*':
                    level.append((r,c))
                    visitied.add((r,c))
                    break
        step = 1
        while level:
            tmp = level[:]
            level.clear()
            rr = [0,0,1,-1]
            cc = [1,-1,0,0]
            for r,c in tmp:
                for i in range(4):
                    newR = r+rr[i]
                    newC = c+cc[i]
                    if 0<=newR<rowCnt and 0<=newC<colCnt:
                        if grid[newR][newC] == '#':
                            return step
                        elif grid[newR][newC] == 'O' and (newR,newC) not in visitied:
                            level.append((newR,newC))
                            visitied.add((newR,newC))
            step += 1
        return -1