class Solution:
    # TC: O(mn) SC:O(m+n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
       
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            if i in row:
                matrix[i] = [0]*n
        for i in range(n):
            if i in col:
                for j in range(m):
                    matrix[j][i] = 0
    

    # use first row and col as flag. TC: O(mn) SC:O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # record row 0 and col 0
        col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break

        row0 = False
        for i in range(n):
            if matrix[0][i] == 0:
                row0 = True
                break

        # record the flag
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] =0
                    matrix[0][j] = 0
        # update the sub-square by flag
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n

        # update row0 and col0
        if row0:
            matrix[0] = [0]*n
        if col0:
            for i in range(m):
                matrix[i][0] = 0
                
    