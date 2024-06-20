class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        # find row index, the last index smaller than target
        # TTTT'T'FFFFF
        left = -1
        right = rowCnt-1
        while left < right:
            mid = (left+right+1)//2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid-1
        if left == -1:
            return False
        
        # find col index
        r = left
        left = 0
        right = colCnt-1
        while left <= right:
            mid = (left+right)//2
            if matrix[r][mid] > target:
                right = mid-1
            elif matrix[r][mid] < target:
                left = mid+1
            else:
                return True
        return False
