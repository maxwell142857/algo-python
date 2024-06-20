class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        n = len(board)
        for i in range(n):
            have = set()
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in have:
                    have.add(board[i][j])
                else:
                    return False
        # check col
        for i in range(n):
            have = set()
            for j in range(n):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in have:
                    have.add(board[j][i])
                else:
                    return False
                
        def checkSquare(r,c):
            have = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] not in have:
                        have.add(board[i][j])
                    else:
                        return False
            return True
        
        # check square:
        for i in range(0,n,3):
            for j in range(0,n,3):
                if not checkSquare(i,j):
                    return False
        return True