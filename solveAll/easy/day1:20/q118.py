class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for level in range(1,numRows):
            cur = []
            cur.append(1)
            for i in range(1,level):
                cur.append(ans[level-1][i-1]+ans[level-1][i])
            cur.append(1)
            ans.append(cur[:])
        return ans
