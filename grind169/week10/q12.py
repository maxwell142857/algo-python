class Solution:
    # greedy,dont work, can only pass certain situation
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        def squareIndex(r,c):
            # 0 1 2
            # 3 4 5
            # 6 7 8
            if r<3:
                if c<3:
                    return 0
                elif c<6:
                    return 3
                else:
                    return 6
            elif r<6:
                if c<3:
                    return 1
                elif c<6:
                    return 4
                else:
                    return 7
            else:
                if c<3:
                    return 2
                elif c<6:
                    return 5
                else:
                    return 8
        
        # init
        cnt = 0
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    cnt += 1
                    val = int(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[squareIndex(r,c)].add(val)
        
        # fill 
        while cnt != 81:
            for r in range(9):
                for c in range(9):
                    candidate = []
                    if board[r][c] == '.':
                        for val in range(1,10):
                            if (val not in rows[r]) and (val not in cols[c]) and (val not in squares[squareIndex(r,c)]):
                                candidate.append(val)
                        if len(candidate) == 1:
                            board[r][c] = str(candidate[0])
                            rows[r].add(candidate[0])
                            cols[c].add(candidate[0])
                            squares[squareIndex(r,c)].add(candidate[0])
                            cnt += 1
    
    # search
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        def squareIndex(r,c):
            # 0 1 2
            # 3 4 5
            # 6 7 8
            if r<3:
                if c<3:
                    return 0
                elif c<6:
                    return 3
                else:
                    return 6
            elif r<6:
                if c<3:
                    return 1
                elif c<6:
                    return 4
                else:
                    return 7
            else:
                if c<3:
                    return 2
                elif c<6:
                    return 5
                else:
                    return 8
        
        def isLegal(r,c,val):
            return (val not in rows[r]) and (val not in cols[c]) and (val not in squares[squareIndex(r,c)])
        
        def add(r,c,val):
            board[r][c] = str(val)
            rows[r].add(val)
            cols[c].add(val)
            squares[squareIndex(r,c)].add(val)

        def remove(r,c):
            val = int(board[r][c])
            rows[r].remove(val)
            cols[c].remove(val)
            squares[squareIndex(r,c)].remove(val)
            board[r][c] = '.'

        # init
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[squareIndex(r,c)].add(val)
        
        
        def fill(r,c):
            if c != 8:
                nextP = (r,c+1)
            else:
                if r == 8:
                    nextP = (-1,-1)
                else:
                    nextP = (r+1,0)

            if board[r][c] != '.':
                if nextP[0] == -1:
                    return True
                return fill(nextP[0],nextP[1])
            else:
                # fill this position
                for val in range(1,10):
                    if isLegal(r,c,val):
                        add(r,c,val)
                        if nextP[0] == -1:
                            return True
                        
                        result = fill(nextP[0],nextP[1])
                        if result:
                            return True
                        else:
                            remove(r,c)
                return False
        
        fill(0,0)
