class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        xx = [1,-1,0,0]
        yy = [0,0,-1,1]
        rowCnt = len(board)
        colCnt = len(board[0])

        find = False
        def DFS(i,j,index):
            nonlocal find
            if find:
                return
            
            if board[i][j] == word[index]:
                if index == len(word)-1:
                    find = True
                    return
                save = board[i][j]
                board[i][j] = '#'
                for ii in range(4):
                    x = i + xx[ii]
                    y = j + yy[ii]
                    if 0<=x<rowCnt and 0<=y<colCnt:
                        DFS(x,y,index+1)
                board[i][j] = save
        
        for r in range(rowCnt):
            for c in range(colCnt):
                if find:
                    return True
                DFS(r,c,0)
        return find