class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        save = [[False for _ in range(n)] for _ in range(m)]

        def DFS(indexI,indexJ):
            nonlocal m,n
            if board[indexI][indexJ] == 'O' and not save[indexI][indexJ]:
                save[indexI][indexJ] = True
                if indexI-1 >= 0 :
                    DFS(indexI-1,indexJ)
                if indexI+1 < m:
                    DFS(indexI+1,indexJ)
                if indexJ-1 >= 0:
                    DFS(indexI,indexJ-1)
                if indexJ+1 < n:
                    DFS(indexI,indexJ+1)
        
        for i in range(m):
            DFS(i,0)
            DFS(i,n-1)
        for i in range(n):
            DFS(0,i)
            DFS(m-1,i)
        for i in range(m):
            for j in range(n):
                if not save[i][j]:
                    board[i][j] = 'X'