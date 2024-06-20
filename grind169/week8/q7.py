class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        isRow0 = False
        isCol0 = False
        for j in range(colCnt):
            if matrix[0][j] == 0:
                isRow0 = True
                break
        for i in range(rowCnt):
            if matrix[i][0] == 0:
                isCol0 = True
                break
        
        # mark the col or row
        for i in range(1,rowCnt):
            for j in range(1,colCnt):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # update row
        for i in range(1,rowCnt):
            if matrix[i][0] == 0:
                for j in range(1,colCnt):
                    matrix[i][j] = 0
        # update col
        for j in range(1,colCnt):
            if matrix[0][j] == 0:
                for i in range(1,rowCnt):
                    matrix[i][j] = 0
        # update the col0 and row0
        if isCol0:
            for i in range(rowCnt):
                matrix[i][0] = 0
        if isRow0:
            for j in range(colCnt):
                matrix[0][j] = 0


