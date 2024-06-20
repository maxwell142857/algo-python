class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rowCnt= len(image)
        colCnt = len(image[0])
        visited = [[False]*colCnt for _ in range(rowCnt)]
        vector = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def fill(r,c):
            visited[r][c] = True
            val = image[r][c]
            image[r][c] = color
            for i in range(4):
                rr = r+vector[i][0]
                cc = c+vector[i][1]
                if 0 <= rr < rowCnt and 0 <= cc < colCnt and not visited[rr][cc] and image[rr][cc] == val:
                    fill(rr,cc)

        fill(sr,sc)
        return image
            
