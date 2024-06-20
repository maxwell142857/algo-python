class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCnt = len(grid)
        colCnt = len(grid[0])
        r_ = [0,0,-1,1]
        c_ = [1,-1,0,0]
        ans = 0
        for i in range(rowCnt):
            for j in range(colCnt):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] == '0'
                    stack = [(i,j)]
                    while stack:
                        location = stack.pop()
                        for k in range(4):
                            newR = location[0]+r_[k]
                            newC = location[1]+c_[k]
                            if 0<=newR<rowCnt and 0<=newC<colCnt and grid[newR][newC] == '1':
                                grid[newR][newC] = '0'
                                stack.append((newR,newC))
        return ans
