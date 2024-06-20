class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        modified = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                count = countAlive(board,i,j,m,n)
                if board[i][j] == 0:
                    if count == 3:
                        modified[i][j] = 1
                else:
                    if count == 2 or count == 3:
                        modified[i][j] = 1
                    else:
                        modified[i][j] = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = modified[i][j]
def countAlive(board,i,j,m,n):
    startI = max(0,i-1)
    endI = min(m-1,i+1)
    startJ = max(0,j-1)
    endJ = min(n-1,j+1)
    count = 0
    for ii in range(startI,endI+1):
        for jj in range(startJ,endJ+1):
            if board[ii][jj] == 1:
                count += 1
    if board[i][j] == 1:
        count -= 1
    return count