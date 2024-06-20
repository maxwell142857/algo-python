class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        rowCnt = len(land)
        colCnt = len(land[0])
        for r in range(rowCnt):
            for c in range(colCnt):
                if land[r][c] == 1:
                    rl = 1
                    cl = 1
                    while r+rl-1< rowCnt and land[r+rl-1][c] == 1:
                        rl += 1
                    rl -= 1
                    while c+cl-1< colCnt and land[r][c+cl-1] == 1:
                        cl += 1
                    cl -= 1
                    for i in range(rl):
                        for j in range(cl):
                            land[r+i][c+j] = 0
                    ans.append((r,c,r+rl-1,c+cl-1))
        return ans
