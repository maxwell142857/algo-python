class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        find = False

        #(r,c) is a legal address, check whether char in this index match word[index]
        def DFS(r,c,index):
            nonlocal find
            
            if board[r][c] != word[index]:
                return
            else:
                if index == len(word)-1:
                    find = True
                    return
                
                rBias = [0,0,-1,1]
                cBias = [1,-1,0,0]
                charSave = board[r][c]
                board[r][c] = '#'
                for i in range(4):
                    rr = r+rBias[i]
                    cc = c+cBias[i]
                    if 0<=rr<len(board) and 0<=cc<len(board[0]):
                        DFS(rr,cc,index+1)
                
                board[r][c] = charSave
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                DFS(i,j,0)
                if find:
                    return True
        return False
        