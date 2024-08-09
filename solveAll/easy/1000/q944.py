class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rowCnt = len(strs)
        colCnt = len(strs[0])
        ans = 0
        for c in range(colCnt):
            for r in range(1,rowCnt):
                if strs[r-1][c] > strs[r][c]:
                    ans += 1
                    break
        return ans