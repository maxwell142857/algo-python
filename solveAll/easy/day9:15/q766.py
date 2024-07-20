class Solution:
    # check each diagonal
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])

        def checkDiagonal(r,c):
            val = matrix[r][c]
            while r<rowCnt and c<colCnt:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1
            return True
        
        # check the first col
        for r in range(rowCnt):
            if not checkDiagonal(r,0):
                return False
        # check the first row
        for c in range(colCnt):
            if not checkDiagonal(0,c):
                return False
        return True
    

    # Group by Category
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        id2val = {}
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        for r in range(rowCnt):
            for c in range(colCnt):
                if r-c not in id2val:
                    id2val[r-c] = matrix[r][c]
                else:
                    if id2val[r-c] != matrix[r][c]:
                        return False
        return True