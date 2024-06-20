from collections import deque


class Solution:
    # dfs
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowCnt = len(heights)
        colCnt = len(heights[0])
        reachableP = set()
        reachableA = set()

        def checkReach(r,c,mySet):
            mySet.add((r,c))
            rr = [1,-1,0,0]
            cc = [0,0,1,-1]
            for i in range(4):
                newR = r+rr[i]
                newC = c+cc[i]
                if 0<=newR<rowCnt and 0<=newC<colCnt and (newR,newC) not in mySet and heights[newR][newC] >= heights[r][c]:
                    checkReach(newR,newC,mySet)
        
        for r in range(rowCnt):
            checkReach(r,0,reachableP)
            checkReach(r,colCnt-1,reachableA)
        for c in range(colCnt):
            checkReach(0,c,reachableP)
            checkReach(rowCnt-1,c,reachableA)
        
        return list(reachableA & reachableP)
    
    # bfs, mark element when pop
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowCnt = len(heights)
        colCnt = len(heights[0])
        reachableP = set()
        reachableA = set()

        def BFS(queue,mySet):
    
            
            rr = [1,-1,0,0]
            cc = [0,0,1,-1]

            while queue:
                r = queue[0][0]
                c = queue[0][1]
                mySet.add((r,c))
                queue.popleft()
                for i in range(4):
                    newR = r+rr[i]
                    newC = c+cc[i]
                    if 0<=newR<rowCnt and 0<=newC<colCnt and (newR,newC) not in mySet and heights[newR][newC] >= heights[r][c]:
                        queue.append((newR,newC))
        queueP = deque()
        queueA = deque()
        for r in range(rowCnt):
            queueP.append((r,0))
            queueA.append((r,colCnt-1))
        for c in range(colCnt):
            queueP.append((0,c))
            queueA.append((rowCnt-1,c))

        BFS(queueA,reachableA)
        BFS(queueP,reachableP)
        return list(reachableA & reachableP)
    
    # bfs, mark element when push
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowCnt = len(heights)
        colCnt = len(heights[0])
        reachableP = set()
        reachableA = set()

        def BFS(queue,mySet):
    
            
            rr = [1,-1,0,0]
            cc = [0,0,1,-1]

            while queue:
                r = queue[0][0]
                c = queue[0][1]
                queue.popleft()
                for i in range(4):
                    newR = r+rr[i]
                    newC = c+cc[i]
                    if 0<=newR<rowCnt and 0<=newC<colCnt and (newR,newC) not in mySet and heights[newR][newC] >= heights[r][c]:
                        queue.append((newR,newC))
                        mySet.add((newR,newC))
        queueP = deque()
        queueA = deque()
        for r in range(rowCnt):
            queueP.append((r,0))
            reachableP.add((r,0))
            queueA.append((r,colCnt-1))
            reachableA.add((r,colCnt-1))
        for c in range(colCnt):
            queueP.append((0,c))
            reachableP.add((0,c))
            queueA.append((rowCnt-1,c))
            reachableA.add((rowCnt-1,c))

        BFS(queueA,reachableA)
        BFS(queueP,reachableP)
        return list(reachableA & reachableP)