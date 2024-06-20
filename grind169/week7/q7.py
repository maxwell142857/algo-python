class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x==0 and y==0:
            return 0
        xx = [-2,-2,-1,-1, 1, 1, 2, 2]
        yy = [ 1,-1, 2,-2, 2,-2, 1,-1]
        step = 1
        visited = set((0,0))
        level = deque([(0,0)])
        while level:
            l = len(level)
            for _ in range(l):
                cur = level.popleft()
                for i in range(8):
                    newx = cur[0]+xx[i]
                    newy = cur[1]+yy[i]
                    if (newx,newy) not in visited:
                        visited.add((newx,newy))
                        if newx == x and newy == y:
                            return step
                        level.append((newx,newy))
            step += 1
        return -1


