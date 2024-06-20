class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        IMPOSSIBLE = 101
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        ans = []
        iPlus = [0,1,0,-1]
        jPlus = [1,0,-1,0]
        iIndex = 0
        jIndex = -1
        index = 0
        cnt = rowCnt*colCnt
        while cnt != 0:
            if 0<=iIndex+iPlus[index]<rowCnt and 0<=jIndex+jPlus[index]<colCnt and \
            matrix[iIndex+iPlus[index]][jIndex+jPlus[index]] != IMPOSSIBLE:
                ans.append(matrix[iIndex+iPlus[index]][jIndex+jPlus[index]])
                cnt -= 1
                matrix[iIndex+iPlus[index]][jIndex+jPlus[index]] = IMPOSSIBLE
                iIndex += iPlus[index]
                jIndex += jPlus[index]
            else:
                # change direction
                index = (index+1)%4

        return ans
