class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        pointer = root
        h = 0
        while pointer.left:
            pointer = pointer.left
            h += 1
        lastLevelNodeCnt = pow(2,h)

        def checkExist(number):
            standard = lastLevelNodeCnt
            pointer = root
            level = 0
            while level < h:
                if number <= standard//2:
                    pointer = pointer.left
                else:
                    number -= standard//2
                    pointer = pointer.right
                standard //= 2
                level += 1
            return pointer
        
        left = 1
        right = lastLevelNodeCnt
        mid = (left+right)//2
        while left < right:
            mid = (left+right+1)/2
            if checkExist(mid):
                left = mid
            else:
                right = mid-1
        return mid+pow(2,h)-1

