class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rowCnt = len(room)
        colCnt = len(room[0])
        cnt = 0
        visited = set() # (row,col,direction)
        cleaned = set() # (row,col)
        index = 0
        def clean(r,c):
            nonlocal cnt,index
            if (r,c) not in cleaned:
                cleaned.add((r,c))
            visited.add((r,c,index))
            findWay = False
            for i in range(4):
                nextR = r+directions[(index+i)%4][0]
                nextC = c+directions[(index+i)%4][1]
                if 0<=nextR<rowCnt and 0<=nextC<colCnt and room[nextR][nextC] == 0:
                    if (nextR,nextC,(index+i)%4) in visited:
                        # already visit this grid in same direction
                        # route will repeat
                        return
                    findWay = True
                    index = (index+i)%4
                    break
            if findWay:
                clean(r+directions[index][0],c+directions[index][1])
            else:
                return
        
        clean(0,0)
        return len(cleaned)