from queue import Queue
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def number2location(number):
            row = (number-1)//n
            col = (number-1)%n
            if row%2 == 1:
                # from left to right
                col = n-1-col
            row = n-1-row
            return [row,col]
                
        # bfs
        myQueue = []
        visited = set()
        myQueue.append(1)
        visited.add(1)
        cnt = 0
        while myQueue:
            nextLevel = []
            cnt += 1
            for location in myQueue:
                for next in range(location+1,min(location+6,n*n)):
                    r,c = number2location(next)
                    if board[r][c] != -1:
                        next = board[r][c]
                    if next not in visited:
                        nextLevel.append(next)   
                        visited.add(next)
                    if next == n*n:
                        return cnt
            myQueue = nextLevel
        return -1