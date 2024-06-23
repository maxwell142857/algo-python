class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rCnt = len(grid)
        cCnt = len(grid[0])
        rMin,cMin = rCnt,cCnt
        rMax,cMax = 0,0
        for r in range(rCnt):
            for c in range(cCnt):
                if grid[r][c]:
                    rMin = min(rMin,r)
                    rMax = max(rMax,r)
                    cMin = min(cMin,c)
                    cMax = max(cMax,c)
        return (rMax-rMin+1)*(cMax-cMin+1)