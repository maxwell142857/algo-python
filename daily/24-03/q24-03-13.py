class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        leftSum,rightSum = 0,0
        while left <= right:
            if leftSum > rightSum:
                rightSum += right
                right -= 1
            elif leftSum < rightSum:
                leftSum += left
                left += 1
            else:
                if left == right:
                    return left
                else:
                    rightSum += right
                    right -= 1
        return -1
