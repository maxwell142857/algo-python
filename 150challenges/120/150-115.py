class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCnt = len(matrix)
        colCnt = len(matrix[0])
        left = 0
        right = rowCnt-1
        while left < right:
            mid = (left+right+1)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid
        
        if matrix[left][0] > target:
            return False
        
        row = left
        left = 0
        right = colCnt-1
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] >target:
                right = mid-1
            else:
                left = mid+1
        return False