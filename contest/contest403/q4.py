class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def check1(start,end) -> int:
            rMin,cMin = end[0],end[1]
            rMax,cMax = 0,0
            find = False
            for r in range(start[0],end[0]):
                for c in range(start[1],end[1]):
                    if grid[r][c]:
                        find = True
                        rMin = min(rMin,r)
                        rMax = max(rMax,r)
                        cMin = min(cMin,c)
                        cMax = max(cMax,c)
            if not find:
                return 0
            else:
                return (rMax-rMin+1)*(cMax-cMin+1)
            
        def check2(start,end):
            ans = float('inf')
            for r in range(start[0],end[0]):
                ans = min(ans,check1(start,(r,end[1]))+check1((r,start[1]),end))
            for c in range(start[1],end[1]):
                ans = min(ans,check1(start,(end[0],c))+check1((start[0],c),end))
            return ans

        def check3(start,end):
            ans = float('inf')
            for r in range(start[0],end[0]):
                ans = min(ans,check1(start,(r,end[1]))+check2((r,start[1]),end))
                ans = min(ans,check2(start,(r,end[1]))+check1((r,start[1]),end))
            for c in range(start[1],end[1]):
                ans = min(ans,check1(start,(end[0],c))+check2((start[0],c),end))
                ans = min(ans,check2(start,(end[0],c))+check1((start[0],c),end))
            return ans
        
        rCnt = len(grid)
        cCnt = len(grid[0])

        
        return check3((0,0),(rCnt,cCnt))
# [[0,0,1],[1,0,1],[0,0,0],[1,0,1]] 6