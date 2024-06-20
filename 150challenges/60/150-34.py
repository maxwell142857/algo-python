class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            used = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in used:
                        return False
                    else:
                        used.add(board[i][j])
        # check column
        for i in range(9):
            used = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in used:
                        return False
                    else:
                        used.add(board[j][i])
        # check square
        for startR in range(0,9,3):
            for startC in range(0,9,3):
                used = set()
                for biasR in range(3):
                    for biasC in range(3):
                        target = board[startR+biasR][startC+biasC]
                        if target != '.':
                            if target in used:
                                return False
                            else:
                                used.add(target)
        return True