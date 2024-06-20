from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        biasR = [0,0,-1,1]
        biasC = [1,-1,0,0]
        distance = [[-1]*n for _ in range(n)]
        level = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    level.append((i,j))
        
        cnt = 0
        while level:
            l = len(level)
            for i in range(l):
                r,c = level.popleft()
                if distance[r][c] == -1:
                    distance[r][c] = cnt
                    
                    for b in range(4):
                        rr = r+biasR[b]
                        cc = c+biasC[b]
                        if 0<=rr<n and 0<=cc<n and distance[rr][cc] == -1:
                            level.append((rr,cc))
            cnt += 1
        
        def DFS(r,c,minVal,visited):
            if distance[r][c] < minVal:
                return False
            
            if r==n-1 and c==n-1:
                return True
            
            result = False
            for b in range(4):
                rr = r+biasR[b]
                cc = c+biasC[b]
                if 0<=rr<n and 0<=cc<n and (rr,cc) not in visited:
                    visited.add((rr,cc))
                    result = result or DFS(rr,cc,minVal,visited)
                    # visited.remove((rr,cc))
            return result
            

        # TTFFFFF
        left = 0
        right = 2*n
        
        while left<right:
            mid = (left+right+1)//2
            visited = set()
            if DFS(0,0,mid,visited):
                left = mid
            else:
                right = mid-1
        
        return left

        

