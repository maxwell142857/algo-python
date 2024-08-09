class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        l = 1
        twice = False
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        dIndex = 0
        r = rStart
        c = cStart
        val = 1
        ans = [[rStart,cStart]]
        while val != rows*cols:
            for _ in range(l):
                r += direction[dIndex][0]
                c += direction[dIndex][1]
                if 0<=r<rows and 0<=c<cols:
                    ans.append([r,c])
                    val += 1
            dIndex = (dIndex+1)%4
            if twice:
                l += 1
                twice = False
            else:
                twice = True
        return ans



