class Solution:
    # O(m^2*n)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        rightL = [[0]*colCnt for _ in range(rowCnt)]
        for r in range(rowCnt):
            if matrix[r][colCnt-1] == '1':
                rightL[r][colCnt-1] = 1
            for c in range(colCnt-2,-1,-1):
                if matrix[r][c] == '1':
                    rightL[r][c] = rightL[r][c+1]+1
        ans = 0
        for r in range(rowCnt):
            for c in range(colCnt):
                minL = float('inf')
                for rBias in range(rowCnt):
                    if r+rBias == rowCnt:
                        break
                    minL = min(minL,rightL[r+rBias][c])
                    ans = max(ans,minL*(rBias+1))
        return ans
    
    # O(mn)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            firstLessIndex = [0]*n
            firstLessIndex[0] = -1
            for i in range(1,n):
                p = i-1 
                while heights[p]>=heights[i]:
                    p = firstLessIndex[p]
                    if p == -1:
                        break
                firstLessIndex[i] = p

            lastLessIndex = [0]*n
            lastLessIndex[-1] = n
            for i in range(n-2,-1,-1):
                p = i+1 
                while heights[p]>=heights[i]:
                    p = lastLessIndex[p]
                    if p == n:
                        break
                lastLessIndex[i] = p
 
            ans = 0
            for i in range(n):
                ans = max(ans,(lastLessIndex[i]-firstLessIndex[i]-1)*heights[i])
            return ans

        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        heights = [0]*colCnt
        for i in range(colCnt):
            if matrix[0][i] == '1':
                heights[i] = 1
        
        ans = largestRectangleArea(heights)
        for r in range(1,rowCnt):
            for c in range(0,colCnt):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            ans = max(ans,largestRectangleArea(heights))
        return ans
        
    