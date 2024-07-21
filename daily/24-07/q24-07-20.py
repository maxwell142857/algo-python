class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rowCnt = len(rowSum)
        colCnt = len(colSum)
        ans = [[0]*colCnt for _ in range(rowCnt)]
        pCol = 0
        for r in range(rowCnt):
            curRowVal = rowSum[r]
            while curRowVal:
                if colSum[pCol] >= curRowVal:
                    ans[r][pCol] = curRowVal
                    colSum[pCol] -= curRowVal
                    if colSum[pCol] == 0:
                        pCol += 1
                    break
                else:
                    ans[r][pCol] = colSum[pCol]
                    curRowVal -= colSum[pCol]
                    pCol += 1
        return ans

