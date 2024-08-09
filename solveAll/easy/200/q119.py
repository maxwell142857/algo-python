class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        ans = [[1],[]]
        for level in range(1,numRows+1):
            cur = []
            cur.append(1)
            for i in range(1,level):
                cur.append(ans[(level+1)%2][i-1]+ans[(level+1)%2][i])
            cur.append(1)
            ans[level%2] = cur[:]
        return ans[numRows%2]
