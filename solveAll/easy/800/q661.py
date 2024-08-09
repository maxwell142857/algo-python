class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rowCnt = len(img)
        colCnt = len(img[0])
        ans = [[0]*colCnt for _ in range(rowCnt)]
        def caculate(r,c):
            sum = 0
            cnt = 0
            for i in range(max(0,r-1),min(rowCnt,r+2)):
                for j in range(max(0,c-1),min(colCnt,c+2)):
                    sum += img[i][j]
                    cnt += 1
            return sum//cnt
        for r in range(rowCnt):
            for c in range(colCnt):
                ans[r][c] = caculate(r,c)
        return ans