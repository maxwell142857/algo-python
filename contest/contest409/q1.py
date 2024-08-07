class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)

    def adjacentSum(self, value: int) -> int:
        r,c = self.find(value)
        bias = [[1,0],[-1,0],[0,1],[0,-1]]
        return self.calculate(r,c,bias)

    def diagonalSum(self, value: int) -> int:
        r,c = self.find(value)
        bias = [[1,1],[-1,1],[1,-1],[-1,-1]]
        return self.calculate(r,c,bias)

    def find(self,val):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == val:
                    return [i,j]
                
    def calculate(self,r,c,bias):
        result = 0
        for rr,cc in bias:
            newR = r+rr
            newC = c+cc
            if 0<=newR<self.n and 0<=newC<self.n:
                result += self.grid[newR][newC]
        return result

        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)