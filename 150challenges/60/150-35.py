class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        directionIndex = 0
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        r,c = 0,0
        cnt = m*n
        while True:
            ans.append(matrix[r][c])
            cnt -= 1
            if cnt == 0:
                return ans
            matrix[r][c] = 101 # imposssible value
            if (r+direction[directionIndex][0]<0 or r+direction[directionIndex][0]>=m or 
                c+direction[directionIndex][1] <0 or c+direction[directionIndex][1] >=n or
                matrix[r+direction[directionIndex][0]][c+direction[directionIndex][1]] == 101):
                directionIndex = (directionIndex+1)%4
            r += direction[directionIndex][0]
            c += direction[directionIndex][1]
